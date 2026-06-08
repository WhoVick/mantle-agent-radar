# Mainnet Deployment Plan

## Goal

Qualify for the **20 x $1,000 Finalist & Deployment** path and strengthen final judging by deploying the proof contract on Mantle mainnet.

## Contract

`contracts/SignalRegistry.sol`

## What It Records

- `signalHash`: hash of the off-chain signal payload.
- `agentId`: bytes32 identity for Mantle Agent Radar.
- `signalType`: alpha, risk, ecosystem, competitor, deadline.
- `confidence`: 0-100 score.
- `reporter`: wallet address.
- `timestamp`: block timestamp.

## Deployment Requirements

- Wallet with enough MNT for gas.
- Mantle RPC.
- Solidity deployment tool: Foundry, Hardhat, Remix, or DoraHacks-friendly online IDE.

## Fastest Path

Use Remix:

1. Open `contracts/SignalRegistry.sol`.
2. Compile with Solidity `0.8.24`.
3. Connect wallet to Mantle mainnet.
4. Deploy `SignalRegistry`.
5. Commit at least one sample signal hash.
6. Put Mantlescan contract URL into DoraHacks submission.

## Sample Signal Hash Flow

1. Pick the top signal from `web/data/signals.json`.
2. Serialize stable fields: `id`, `title`, `summary`, `confidence`, `evidence`.
3. Compute `keccak256`.
4. Call `commitSignal(signalHash, agentId, signalType, confidence)`.

## Why This Helps

The chat confirmed testnet counts, but mainnet deployment is considered better for final winners. This is a small contract, low risk, and directly improves the Technical, Ecosystem fit, and Verifiability story.

