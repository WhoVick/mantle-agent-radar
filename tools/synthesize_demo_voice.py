from __future__ import annotations

import asyncio
import json
import subprocess
from pathlib import Path

import edge_tts


ROOT = Path(__file__).resolve().parents[1]
SEGMENT_DIR = ROOT / "assets" / ".demo-voice-v4"
OUTPUT_MP3 = ROOT / "submission" / "demo-voiceover-v4.mp3"
OUTPUT_TXT = ROOT / "submission" / "demo-voiceover-v4.txt"
MANIFEST = ROOT / "submission" / "demo-voiceover-v4.json"

FFMPEG = Path(
    r"C:\Users\User\AppData\Local\Microsoft\WinGet\Packages"
    r"\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe"
    r"\ffmpeg-8.1.1-full_build\bin\ffmpeg.exe"
)
FFPROBE = FFMPEG.with_name("ffprobe.exe")

VOICE_CANDIDATES = [
    "en-US-AvaMultilingualNeural",
    "en-US-JennyNeural",
    "en-US-AriaNeural",
    "en-GB-SoniaNeural",
]

SEGMENTS = [
    {
        "step": "Step 1",
        "title": "Start with scattered context",
        "text": "Mantle alpha rarely starts as a clean dashboard. It appears in hackathon rules, Telegram replies, judging criteria, and on-chain receipts.",
    },
    {
        "step": "Step 2",
        "title": "Click scan",
        "text": "Radar pulls those fragments into one inbox. Here I click scan, and the agent starts turning messy context into structured signals.",
    },
    {
        "step": "Step 3",
        "title": "Rank the feed",
        "text": "The ranked feed appears. Each card has a confidence score, evidence tags, and the source it came from.",
    },
    {
        "step": "Step 4",
        "title": "Filter urgent edge",
        "text": "Now I filter for deadline and deployment edge, because those signals can change our next action fastest.",
    },
    {
        "step": "Step 5",
        "title": "Open the top signal",
        "text": "Opening the top signal shows the reasoning: what happened, why it matters, the evidence, and the suggested move.",
    },
    {
        "step": "Step 6",
        "title": "Show the scoring logic",
        "text": "On the right, you can see raw source text becoming a scored signal. Source quality, urgency, novelty, and utility are all part of the score.",
    },
    {
        "step": "Step 7",
        "title": "Commit proof on Mantle",
        "text": "For high-confidence signals, Radar creates a hash and commits it through SignalRegistry on Mantle mainnet.",
    },
    {
        "step": "Step 8",
        "title": "Verify the proof trail",
        "text": "That gives judges a public proof trail: contract address, transaction hash, and the exact signal hash can be checked later.",
    },
    {
        "step": "Step 9",
        "title": "End with the product path",
        "text": "So the product path is simple: collect early context, rank it, explain it, and prove the best signals on-chain.",
    },
]


def run(args: list[str]) -> str:
    completed = subprocess.run(args, check=True, capture_output=True, text=True)
    return completed.stdout.strip()


def duration_seconds(path: Path) -> float:
    return float(
        run(
            [
                str(FFPROBE),
                "-v",
                "error",
                "-show_entries",
                "format=duration",
                "-of",
                "default=noprint_wrappers=1:nokey=1",
                str(path),
            ]
        )
    )


async def synthesize_with_voice(voice: str) -> list[Path]:
    paths: list[Path] = []
    for index, segment in enumerate(SEGMENTS, 1):
        path = SEGMENT_DIR / f"segment-{index:02d}.mp3"
        communicate = edge_tts.Communicate(
            segment["text"],
            voice,
            rate="-4%",
            pitch="-1Hz",
            volume="+0%",
        )
        await communicate.save(str(path))
        paths.append(path)
    return paths


async def synthesize_segments() -> tuple[str, list[Path]]:
    SEGMENT_DIR.mkdir(parents=True, exist_ok=True)
    for stale in SEGMENT_DIR.glob("segment-*.mp3"):
        stale.unlink()

    last_error: Exception | None = None
    for voice in VOICE_CANDIDATES:
        try:
            return voice, await synthesize_with_voice(voice)
        except Exception as error:  # noqa: BLE001 - keep trying candidate voices.
            last_error = error
            for stale in SEGMENT_DIR.glob("segment-*.mp3"):
                stale.unlink()
    raise RuntimeError(f"Could not synthesize voiceover: {last_error}")


async def main() -> None:
    if not FFMPEG.exists() or not FFPROBE.exists():
        raise RuntimeError("FFmpeg/ffprobe binaries were not found.")

    voice, segment_paths = await synthesize_segments()
    list_path = SEGMENT_DIR / "concat.txt"
    list_path.write_text(
        "\n".join(f"file '{path.as_posix()}'" for path in segment_paths) + "\n",
        encoding="utf-8",
    )

    run(
        [
            str(FFMPEG),
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(list_path),
            "-af",
            "acompressor=threshold=-18dB:ratio=2.2:attack=12:release=160,loudnorm=I=-16:TP=-1.5:LRA=10",
            "-c:a",
            "libmp3lame",
            "-q:a",
            "3",
            str(OUTPUT_MP3),
        ]
    )

    starts: list[float] = []
    cursor = 0.0
    enriched = []
    for segment, path in zip(SEGMENTS, segment_paths):
        starts.append(cursor)
        length = duration_seconds(path)
        enriched.append({**segment, "start": round(cursor, 2), "duration": round(length, 2)})
        cursor += length

    manifest = {
        "voice": voice,
        "output": str(OUTPUT_MP3),
        "duration": round(duration_seconds(OUTPUT_MP3), 2),
        "segments": enriched,
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    OUTPUT_TXT.write_text("\n\n".join(segment["text"] for segment in SEGMENTS), encoding="utf-8")

    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
