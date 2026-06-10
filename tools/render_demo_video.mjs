import { spawn } from "node:child_process";
import { mkdir, readdir, readFile, rm, writeFile } from "node:fs/promises";
import { existsSync } from "node:fs";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const projectRoot = path.resolve(path.join(path.dirname(fileURLToPath(import.meta.url)), ".."));
const pageArg = process.argv[2] ?? "web/demo-recording.html";
const outputArg = process.argv[3] ?? "submission/mantle-agent-radar-demo.mp4";
const pagePath = path.isAbsolute(pageArg) ? pageArg : path.join(projectRoot, pageArg);
const outputPath = path.isAbsolute(outputArg) ? outputArg : path.join(projectRoot, outputArg);
const frameDir = path.join(projectRoot, "assets", ".demo-video-frames");
const width = 1280;
const height = 720;
const duration = Number(process.env.DEMO_DURATION ?? 72);
const fps = Number(process.env.DEMO_FPS ?? 6);
const concurrency = 3;

const chromeCandidates = [
  process.env.CHROME_PATH,
  "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
  "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
  "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
].filter(Boolean);

const ffmpegCandidates = [
  process.env.FFMPEG_PATH,
  "C:\\Users\\User\\AppData\\Local\\Microsoft\\WinGet\\Packages\\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\\ffmpeg-8.1.1-full_build\\bin\\ffmpeg.exe",
  "ffmpeg"
].filter(Boolean);

function findBinary(candidates) {
  const found = candidates.find((candidate) => candidate === "ffmpeg" || existsSync(candidate));
  if (!found) {
    throw new Error(`No binary found from candidates: ${candidates.join(", ")}`);
  }
  return found;
}

function run(command, args, options = {}) {
  return new Promise((resolve, reject) => {
    const child = spawn(command, args, { stdio: ["ignore", "pipe", "pipe"], ...options });
    let stdout = "";
    let stderr = "";
    child.stdout.on("data", (chunk) => {
      stdout += chunk;
    });
    child.stderr.on("data", (chunk) => {
      stderr += chunk;
    });
    child.on("error", reject);
    child.on("close", (code) => {
      if (code === 0) {
        resolve({ stdout, stderr });
        return;
      }
      reject(new Error(`${command} exited with ${code}\n${stdout}\n${stderr}`));
    });
  });
}

async function prepareFrameDir() {
  const resolvedFrameDir = path.resolve(frameDir);
  if (!resolvedFrameDir.startsWith(projectRoot)) {
    throw new Error(`Unsafe frame directory: ${resolvedFrameDir}`);
  }
  await rm(resolvedFrameDir, { recursive: true, force: true });
  await mkdir(resolvedFrameDir, { recursive: true });
}

async function renderOneFrame(chrome, frameIndex) {
  const seconds = frameIndex / fps;
  const fileName = `frame_${String(frameIndex + 1).padStart(5, "0")}.png`;
  const framePath = path.join(frameDir, fileName);
  const pageUrl = `${pathToFileURL(pagePath).href}?t=${seconds.toFixed(3)}`;
  await run(chrome, [
    "--headless=new",
    "--disable-gpu",
    "--hide-scrollbars",
    "--run-all-compositor-stages-before-draw",
    "--virtual-time-budget=1000",
    `--window-size=${width},${height}`,
    `--screenshot=${framePath}`,
    pageUrl
  ]);
}

async function renderFrames() {
  const chrome = findBinary(chromeCandidates);
  const totalFrames = duration * fps;
  let nextFrame = 0;

  async function worker() {
    while (true) {
      const frameIndex = nextFrame;
      nextFrame += 1;
      if (frameIndex >= totalFrames) {
        return;
      }
      await renderOneFrame(chrome, frameIndex);
      if ((frameIndex + 1) % 60 === 0 || frameIndex + 1 === totalFrames) {
        console.log(`Captured ${frameIndex + 1}/${totalFrames} frames`);
      }
    }
  }

  await Promise.all(Array.from({ length: concurrency }, () => worker()));
}

async function encodeVideo() {
  const ffmpeg = findBinary(ffmpegCandidates);
  await run(ffmpeg, [
    "-y",
    "-framerate",
    String(fps),
    "-i",
    path.join(frameDir, "frame_%05d.png"),
    "-c:v",
    "libx264",
    "-crf",
    "20",
    "-preset",
    "medium",
    "-pix_fmt",
    "yuv420p",
    "-movflags",
    "+faststart",
    outputPath
  ]);
}

async function writeMetadata() {
  const mp4 = await readFile(outputPath);
  const metaPath = outputPath.replace(/\.mp4$/i, ".json");
  await writeFile(
    metaPath,
    JSON.stringify(
      {
        file: outputPath,
        bytes: mp4.length,
        duration_seconds: duration,
        fps,
        resolution: `${width}x${height}`,
        source: pagePath,
        generated_at: new Date().toISOString()
      },
      null,
      2
    )
  );
}

await prepareFrameDir();
await renderFrames();
await encodeVideo();
await writeMetadata();

const frameCount = (await readdir(frameDir)).filter((name) => name.endsWith(".png")).length;
console.log(`Rendered ${outputPath}`);
console.log(`Frames: ${frameCount}`);
