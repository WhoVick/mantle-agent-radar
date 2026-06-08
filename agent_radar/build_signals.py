from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from .models import SourceEvent
from .scoring import rank_signals


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data" / "seed_events.json"
DEFAULT_OUTPUT = ROOT / "web" / "data" / "signals.json"
DEFAULT_JS_OUTPUT = ROOT / "web" / "data" / "signals.js"


def load_events(path: Path) -> list[SourceEvent]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    return [SourceEvent(**item) for item in raw["events"]]


def build_payload(events: list[SourceEvent]) -> dict:
    signals = rank_signals(events)
    return {
        "project": "Mantle Agent Radar",
        "track": "AI Alpha & Data",
        "generated_from": len(events),
        "signals": [asdict(signal) for signal in signals],
        "sources": [asdict(event) for event in events],
        "score_weights": {
            "source_quality": 0.25,
            "mantle_relevance": 0.25,
            "investment_utility": 0.20,
            "urgency": 0.15,
            "novelty": 0.15,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Build Mantle Agent Radar signal JSON.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--js-output", type=Path, default=DEFAULT_JS_OUTPUT)
    args = parser.parse_args()

    events = load_events(args.input)
    payload = build_payload(events)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    serialized = json.dumps(payload, indent=2, ensure_ascii=False)
    args.output.write_text(serialized, encoding="utf-8")
    args.js_output.parent.mkdir(parents=True, exist_ok=True)
    args.js_output.write_text(f"window.SIGNAL_DATA = {serialized};\n", encoding="utf-8")
    print(f"Wrote {len(payload['signals'])} signals to {args.output}")


if __name__ == "__main__":
    main()
