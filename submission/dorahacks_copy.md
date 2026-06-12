# DoraHacks Submission Draft

## Project Name

Mantle Agent Radar

## Track

Track 02 - AI Alpha & Data

## One-liner

An AI intelligence agent that turns Mantle social, ecosystem, and on-chain sources into ranked, explainable, judge-ready alpha signal packets with public Mantle mainnet proof.

## Problem

Mantle builders and investors are flooded with scattered Telegram messages, X posts, DevHub updates, DoraHacks pages, on-chain events, and sponsor notes. Useful alpha often appears early, but it is mixed with noise, hard to verify, and rarely packaged as something a fund, trader, protocol team, or judge can quickly act on.

## Solution

Mantle Agent Radar ingests Mantle-native source events, classifies them as alpha, risk, ecosystem, competitor, deployment, or deadline signals, and scores them by source quality, Mantle relevance, investment utility, urgency, novelty, and evidence strength.

The dashboard then turns each signal into a Judge Packet:

- Why now: the short reason this signal matters today.
- Judge fit: how the signal maps to hackathon criteria and Mantle ecosystem value.
- Investor use: what a fund, trader, or builder could actually do with it.
- Risk control: what should be verified before acting.
- Evidence: source-backed excerpts instead of unsupported claims.
- Copy packet: a one-click summary for judges, investors, or internal research notes.

High-confidence signals can also be committed to Mantle through a lightweight SignalRegistry contract. This creates a timestamped proof that the agent produced the signal hash before it became obvious later.

## What is live now

- Public ranked signal dashboard.
- Judge Packet panel for every signal.
- Evidence excerpts and confidence scoring.
- Mantle mainnet proof strip for the committed top signal.
- Copyable research packet for judges and investors.
- SignalRegistry contract deployed on Mantle mainnet.

## Why Mantle

- The product uses Mantle DevHub, DoraHacks, Telegram/forum intelligence, Mantlescan references, and Mantle agent/ecosystem context.
- Mantle has many parallel information streams right now: AI agents, DeFi, RWA/xStocks, builder incentives, protocol launches, and hackathon activity.
- Radar is built for that early, messy context where useful information appears before it is clean enough for normal dashboards.
- Mantle mainnet is used for proof-of-signal, not just as a logo on the submission.

## Judging Criteria Fit

- Insight value: surfaces actionable early signals from fragmented Mantle sources.
- Data source quality: prioritizes source-backed Mantle-native evidence.
- Investment utility: every signal includes a suggested action and risk check.
- Scalability: source events and scoring weights can extend to more protocols, campaigns, and chains.
- Verifiability: selected signal hashes can be committed on-chain through SignalRegistry.

## Business Model

- Free delayed public dashboard for community visibility.
- Paid real-time alerts for funds, serious traders, Mantle builders, and protocol teams.
- Custom monitoring bots for launches, RWA risks, competitor tracking, deadlines, grants, and smart-money flows.
- Optional proof layer for teams that want timestamped evidence of when a signal was generated.

## Demo

Live demo: https://whovick.github.io/mantle-agent-radar/

GitHub: https://github.com/WhoVick/mantle-agent-radar

Captioned product demo: https://whovick.github.io/mantle-agent-radar/web/demo-captions.html

Mantle mainnet proof:

- SignalRegistry contract: https://mantlescan.xyz/address/0x5A3C88E1DfE4377448337f3795Ddb7C46A2F3088
- First committed signal transaction: https://mantlescan.xyz/tx/0x505a05c21390d91993d8bce153d927629db4e05e96bca8260ac2a743ea478ad9
- Signal hash: 0xa9f5171c0fe010f1f4a09c375b7690972d8f1c3038c01b363b51a6d3291731fe
- Agent ID: 0xa01ff137ec71f15114acd88a208f392ecb6f6ffb728043d75d3ecf51ad8c1d8f

Suggested judge flow:

1. Open the ranked feed and select the top signal.
2. Read the Judge Packet: why now, judge fit, investor use, risk, and proof.
3. Check the evidence excerpts under the packet.
4. Open the Mantlescan transaction for the committed signal hash.
5. Use Copy packet to see the exact investor/judge summary the agent produces.
