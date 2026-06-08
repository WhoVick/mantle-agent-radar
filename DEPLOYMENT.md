# Deployment

## Static Dashboard

The dashboard is static and deploys from `web/`.

Current GitHub Pages demo:

- https://whovick.github.io/mantle-agent-radar/

### Vercel

1. Import the GitHub repository.
2. Use the project root as root directory.
3. Vercel reads `vercel.json`.
4. Build command: `python -m agent_radar.build_signals`
5. Output directory: `web`

### Netlify

Netlify reads `netlify.toml`:

- command: `python -m agent_radar.build_signals`
- publish: `web`

### Local

```powershell
python -m agent_radar.build_signals
python -m http.server 8899 --bind 127.0.0.1 --directory web
```

## Mantle Mainnet Proof Contract

Network:

- Chain ID: `5000`
- Native currency: `MNT`
- RPC: `https://rpc.mantle.xyz`
- Explorer: `https://mantlescan.xyz`

Contract:

- `contracts/SignalRegistry.sol`

Fast deployment:

1. Open Remix.
2. Paste `contracts/SignalRegistry.sol`.
3. Compile with Solidity `0.8.24`.
4. Connect wallet on Mantle mainnet.
5. Deploy.
6. Generate a signal hash:

```powershell
python tools/hash_signal.py --top
```

7. Call `commitSignal(signalHash, agentId, signalType, confidence)`.
8. Add the Mantlescan URL to DoraHacks.

Note: `tools/hash_signal.py` uses stdlib SHA3-256 for deterministic MVP commitments. For exact Ethereum Keccak-256, compute with Foundry or ethers before the final mainnet transaction.
