from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SIGNALS_PATH = ROOT / "web" / "data" / "signals.json"


def canonical_signal(signal: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": signal["id"],
        "signal_type": signal["signal_type"],
        "title": signal["title"],
        "summary": signal["summary"],
        "confidence": signal["confidence"],
        "evidence": signal["evidence"],
    }


def pseudo_keccak256(data: bytes) -> str:
    # Python stdlib ships SHA3-256, not Ethereum's Keccak-256. For the MVP this
    # gives a deterministic commitment hash; use Foundry/ethers for exact
    # keccak256 before a production mainnet transaction.
    return "0x" + hashlib.sha3_256(data).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a deterministic commitment hash for a signal.")
    parser.add_argument("--signal-id", help="Signal id from web/data/signals.json")
    parser.add_argument("--top", action="store_true", help="Use the top-ranked signal")
    args = parser.parse_args()

    data = json.loads(SIGNALS_PATH.read_text(encoding="utf-8"))
    signals = data["signals"]
    if args.top:
        signal = signals[0]
    else:
        if not args.signal_id:
            raise SystemExit("Pass --top or --signal-id")
        signal = next((item for item in signals if item["id"] == args.signal_id), None)
        if signal is None:
            raise SystemExit(f"Signal not found: {args.signal_id}")

    canonical = canonical_signal(signal)
    payload = json.dumps(canonical, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    print(json.dumps({
        "signal_id": signal["id"],
        "signal_type": signal["signal_type"],
        "confidence": signal["confidence"],
        "hash": pseudo_keccak256(payload),
        "agent_id_note": "Use bytes32 agent id, e.g. keccak256('Mantle Agent Radar v0.1') in Remix/ethers.",
        "canonical_payload": canonical,
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

