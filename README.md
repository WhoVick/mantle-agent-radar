# Mantle Agent Radar

AI Alpha & Data agent for the Mantle Turing Test Hackathon 2026.

Live demo: https://whovick.github.io/mantle-agent-radar/

GitHub: https://github.com/WhoVick/mantle-agent-radar

## What It Does

Mantle Agent Radar turns fragmented Mantle ecosystem information into ranked, explainable, investor-grade signals.

It ingests structured events from Mantle-native sources such as DevHub updates, DoraHacks instructions, Telegram/forum intelligence, Mantlescan references, competitor signals, and ecosystem notes. Each event is scored by source quality, Mantle relevance, investment utility, urgency, novelty, and risk.

The dashboard shows:

- Live Mantle mainnet block ingestion through the public JSON-RPC endpoint, with a refresh control and Mantlescan evidence.
- Ranked alpha, risk, deadline, competitor, deployment, and ecosystem signals.
- Evidence trails for every signal.
- Confidence scores and recommended action.
- A proof path for committing high-confidence signals to Mantle mainnet.

## Track

Track 02 - AI Alpha & Data.

Judging fit:

- Insight value: actionable early signals instead of generic summaries.
- Data source quality: Mantle-native official, social, and on-chain references.
- Investment utility: every signal has a concrete action.
- Scalability: modular source events and scoring weights.
- Verifiability: signal hashes can be committed through `SignalRegistry`.

## Repository Map

- `agent_radar/` - signal models, scoring, and build pipeline.
- `data/seed_events.json` - current source-event dataset.
- `web/` - static dashboard.
- `contracts/SignalRegistry.sol` - minimal Mantle proof contract.
- `proof/` - Mantle mainnet proof links and committed signal metadata.
- `tools/hash_signal.py` - deterministic signal hash helper.
- `telegram_monitor/` - read-only Telethon monitor for hackathon chat intelligence.
- `research/` - hackathon brief, opportunity map, Telegram intel, and strategy.
- `submission/` - DoraHacks copy, demo script, X thread, and deployment plan.
- `JUDGES.md` - concise judge-facing explanation.
- `DEPLOYMENT.md` - static dashboard and Mantle deployment notes.

## Commands

```powershell
npm run build
npm run check
npm run hash:top
```

Local preview:

```powershell
npm run preview
```

Open the dashboard and select `Refresh live`. The app reads the latest Mantle mainnet block without an API key, creates a scored live signal, and links the evidence to Mantlescan. If the public RPC is unavailable, the submitted static evidence remains visible.

## Telegram Monitoring

The monitor can use a local `.env` with a dedicated Telegram account and optional proxy:

```dotenv
TELEGRAM_PROXY=socks5://user:password@host:port
```

Do not commit `.env`, session files, phone numbers, API hashes, proxy credentials, or private keys.

## Mainnet Proof

Mantle Agent Radar has a live proof contract on Mantle mainnet:

- Contract: https://mantlescan.xyz/address/0x5A3C88E1DfE4377448337f3795Ddb7C46A2F3088
- First signal commitment: https://mantlescan.xyz/tx/0x505a05c21390d91993d8bce153d927629db4e05e96bca8260ac2a743ea478ad9

The committed signal metadata is stored in `proof/mainnet.json`.
