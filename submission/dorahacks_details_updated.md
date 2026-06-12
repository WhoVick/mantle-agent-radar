## Mantle Agent Radar

I started Mantle Agent Radar while researching this hackathon. A lot of useful Mantle information was not in one clean place. It was spread across DoraHacks pages, Telegram replies, DevHub updates, sponsor notes, on-chain references, and small ecosystem updates.

Some of those details can become real alpha, but they are easy to miss.

Mantle Agent Radar turns that messy layer into a ranked signal feed for people watching the Mantle ecosystem: builders, funds, traders, protocol teams, and hackathon judges.

## What it does

The MVP ingests Mantle-native source events, classifies them as alpha, risk, ecosystem, competitor, deployment, or deadline signals, and scores them by source quality, Mantle relevance, urgency, novelty, investment utility, and evidence strength.

Each signal shows what happened, why it may matter, the supporting evidence, a confidence score, and a suggested action.

The newest version also creates a Judge Packet for every signal:

- Why now: the short reason this signal matters today.
- Judge fit: how the signal maps to hackathon criteria and Mantle ecosystem value.
- Investor use: what a fund, trader, or builder could actually do with it.
- Risk control: what should be verified before acting.
- Evidence: source-backed excerpts instead of unsupported claims.
- Copy packet: a one-click summary for judges, investors, or internal research notes.

## Demo

Live demo:

https://whovick.github.io/mantle-agent-radar/

GitHub:

https://github.com/WhoVick/mantle-agent-radar

Captioned demo:

https://whovick.github.io/mantle-agent-radar/web/demo-captions.html

## Mantle mainnet proof

For high-confidence signals, Radar can hash the signal and commit it through SignalRegistry on Mantle. This gives a timestamped proof that the agent produced the signal before it became obvious later.

SignalRegistry contract:

https://mantlescan.xyz/address/0x5A3C88E1DfE4377448337f3795Ddb7C46A2F3088

First committed signal transaction:

https://mantlescan.xyz/tx/0x505a05c21390d91993d8bce153d927629db4e05e96bca8260ac2a743ea478ad9

Committed signal hash:

0xa9f5171c0fe010f1f4a09c375b7690972d8f1c3038c01b363b51a6d3291731fe

Agent ID:

0xa01ff137ec71f15114acd88a208f392ecb6f6ffb728043d75d3ecf51ad8c1d8f

## Why Mantle

Mantle is moving across AI agents, DeFi, RWA/xStocks, builder incentives, and protocol launches at the same time. A lot of context appears before it becomes visible in normal dashboards.

Radar is built for that early, messy context.

This is why Mantle is not just the chain named in the submission. It is used in the product data sources, the scoring context, and the on-chain proof layer.

## Who it is for

This could be useful for:

- funds and serious traders watching Mantle-native opportunities earlier;
- builders tracking deadlines, grants, launches, and ecosystem movements;
- protocol teams monitoring competitor or risk signals;
- judges who need to understand why a signal matters without reading every source manually.

## Business model

The public dashboard can stay delayed and free.

The paid version would be real-time alerts and custom monitoring bots for funds, traders, Mantle protocol teams, launches, RWA risks, competitor tracking, grant deadlines, and smart-money flows.

## Suggested judge flow

1. Open the ranked feed.
2. Select the top signal.
3. Read the Judge Packet: why now, judge fit, investor use, risk, and proof.
4. Check the evidence excerpts under the packet.
5. Open the Mantlescan transaction for the committed signal hash.
6. Use Copy packet to see the exact investor/judge summary the agent produces.
