# Winning Strategy

## Product

**Mantle Agent Radar**

An AI intelligence agent for Mantle investors and builders. It watches Telegram/social chatter and Mantle-native on-chain events, detects early alpha/anomaly/risk signals, scores them, explains evidence, and commits a hash of each high-confidence signal to Mantle for verifiability.

## Track

Primary track: **Track 02 - AI Alpha & Data**.

Why:

- Judging criteria reward novel insights, data source quality, investment utility, and scalable live pipelines.
- The product can be built quickly as a working MVP.
- The commercial path is obvious: paid intelligence subscription for funds, protocol teams, and serious traders.
- It gives us multiple prize paths: track prize, deployment finalist, UI/UX if dashboard is polished, community voting if X cards are strong.

## Prize Strategy

Target stack:

- **$8,500 Track First Prize**: win Alpha & Data with a real, working agent.
- **$1,000 Deployment Finalist**: deploy a simple signal registry / attestation contract on Mantle mainnet.
- **$8,500 Community Voting**: publish short X threads with live signal cards and tag Mantle.
- Stretch: **$9,000 Grand Champion** if the demo feels production-grade and investment-ready.

## MVP Scope

Must ship:

1. Ingestion:
   - Telegram hackathon/Mantle/social messages.
   - Curated Mantle ecosystem event feed.
   - Optional on-chain RPC watcher.
2. Signal engine:
   - classify alpha / anomaly / risk / ecosystem / competitor / deadline;
   - score novelty, source credibility, urgency, cross-source confirmation, Mantle relevance.
3. Dashboard:
   - ranked signal stream;
   - evidence links;
   - confidence and rationale;
   - investor-ready "why this matters".
4. On-chain proof:
   - simple Solidity contract to record `signalHash`, `agentId`, `signalType`, `confidence`, `timestamp`.
5. Submission package:
   - README, demo script, screenshots, X-ready pitch, DoraHacks copy.

## Scoring Optimization

### Technical, 15

Show an end-to-end working pipeline: source -> agent scoring -> dashboard -> on-chain hash.

### Ecosystem Fit, 10

Use Mantle-native language and assets:

- Mantle mainnet/testnet;
- Mantlescan;
- ERC-8004 Identity Registry;
- Mantle DevHub;
- Mantle tracks/protocols;
- social/on-chain signals from Mantle ecosystem.

### Business Potential, 10

Pitch paid intelligence:

- Free public dashboard for delayed signals.
- Paid real-time alerts for funds, protocol teams, and serious traders.
- Custom monitoring for Mantle protocols.

### Innovation, 10

Differentiate from competitors:

- not a generic quant bot;
- not another RWA vault;
- not just social sentiment;
- unique fusion of social intent, on-chain traces, agent identity, and verifiable alpha cards.

### UX, 5

Build a clean dashboard with one fast workflow: "what happened, why it matters, what to watch next".

### Alpha & Data Part B, 50

- Insight value: show examples that a smart investor would act on.
- Data quality: live Telegram + official sources + Mantle-native on-chain links.
- Investment utility: label each signal with action type: monitor, investigate, de-risk, opportunity.
- Scalability: modular source adapters and scoring config.

## Immediate Build Plan

1. Create `agent_radar/` Python package.
2. Seed it with Telegram intel captured today plus mock Mantle on-chain events.
3. Generate `web/data/signals.json`.
4. Build static dashboard in `web/`.
5. Add `contracts/SignalRegistry.sol`.
6. Add demo script and submission text.

