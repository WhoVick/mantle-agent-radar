# DoraHacks Submission Draft

## Project Name

Mantle Agent Radar

## Track

Track 02 - AI Alpha & Data

## One-liner

An AI intelligence agent that turns Mantle social, ecosystem, and on-chain sources into ranked, explainable, and verifiable investor-grade alpha signals.

## Problem

Mantle builders and investors are flooded with scattered Telegram messages, X posts, DevHub updates, on-chain events, and competitor signals. Valuable alpha appears early, but it is noisy, hard to verify, and rarely packaged as an investor-ready decision.

## Solution

Mantle Agent Radar ingests Mantle-native sources, classifies alpha/risk/ecosystem/competitor/deadline signals, scores them by source quality, Mantle relevance, investment utility, urgency, and novelty, then displays a ranked signal dashboard with evidence and recommended action.

High-confidence signals can be committed to Mantle through a lightweight `SignalRegistry` contract, creating a timestamped proof that the agent generated the signal before it became obvious.

## Why Mantle

- Uses Mantle DevHub, DoraHacks, Telegram, Mantlescan, and Mantle ERC-8004 registry intelligence.
- Designed for Mantle-native protocols, RWA/xStock flows, agent identity, and deployment tracking.
- Includes a Mantle proof contract for signal hash attestations.

## Judging Criteria Fit

- Insight value: surfaces actionable early signals from fragmented sources.
- Data source quality: prioritizes Mantle-native official, social, and on-chain sources.
- Investment utility: every signal includes a recommended investor/builder action.
- Scalability: modular source events and scoring weights can extend to more protocols/chains.
- Verifiability: signal hashes can be committed on-chain.

## Business Model

- Free delayed public dashboard.
- Paid real-time alerts for funds, serious traders, and Mantle protocol teams.
- Custom monitoring bots for protocol launches, RWA risks, competitor tracking, and smart money flows.

## Demo

Live demo: https://whovick.github.io/mantle-agent-radar/

GitHub: https://github.com/WhoVick/mantle-agent-radar

Show:

1. Ranked signal feed.
2. Top signal detail with evidence and scoring.
3. Filtered competitor/risk/deployment signals.
4. `contracts/SignalRegistry.sol` for on-chain proof.
