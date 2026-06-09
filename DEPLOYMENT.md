# Deployment

## Static Dashboard

The dashboard is static and deploys from `web/`.

Current GitHub Pages demo:

- https://whovick.github.io/mantle-agent-radar/
- Proof deployer: https://whovick.github.io/mantle-agent-radar/deploy.html

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
- Live contract: https://mantlescan.xyz/address/0x5A3C88E1DfE4377448337f3795Ddb7C46A2F3088
- First committed signal tx: https://mantlescan.xyz/tx/0x505a05c21390d91993d8bce153d927629db4e05e96bca8260ac2a743ea478ad9

Fast deployment:

1. Open `web/deploy.html` or the public proof deployer URL.
2. Connect Rabby or another injected wallet.
3. Switch to Mantle mainnet.
4. Click `Deploy`.
5. Click `Commit Signal`.
6. Generate a signal hash:

```powershell
python tools/hash_signal.py --top
```

7. Add the Mantlescan contract and transaction URLs to DoraHacks.

Note: `tools/hash_signal.py` uses stdlib SHA3-256 for deterministic MVP commitments. For exact Ethereum Keccak-256, compute with Foundry or ethers before the final mainnet transaction.
