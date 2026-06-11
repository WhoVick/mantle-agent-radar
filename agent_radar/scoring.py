from __future__ import annotations

import hashlib
from collections import Counter
from typing import Iterable

from .models import Signal, SourceEvent


TYPE_KEYWORDS = {
    "alpha": ("alpha", "signal", "smart money", "emerging", "investment", "flow"),
    "risk": ("risk", "depeg", "crash", "compliance", "audit", "safeguard"),
    "ecosystem": ("mantle", "mainnet", "registry", "devhub", "erc8004", "deployment"),
    "competitor": ("building", "project", "buidl", "competitor", "oracle", "vault"),
    "deadline": ("deadline", "jun 15", "submit", "demo day", "winner", "prize"),
}

BASE_SCORES = {
    "telegram": 50,
    "devhub": 80,
    "criteria": 90,
    "mantlescan": 85,
    "dorahacks": 75,
    "x": 55,
}


def stable_id(*parts: str) -> str:
    digest = hashlib.sha256("|".join(parts).encode("utf-8")).hexdigest()
    return digest[:16]


def classify(event: SourceEvent) -> str:
    text = " ".join([event.title, event.text, " ".join(event.tags)]).lower()
    matches = {
        kind: sum(1 for token in tokens if token in text)
        for kind, tokens in TYPE_KEYWORDS.items()
    }
    best, score = Counter(matches).most_common(1)[0]
    return best if score > 0 else "alpha"


def score_event(event: SourceEvent) -> dict[str, int]:
    text = " ".join([event.title, event.text, " ".join(event.tags)]).lower()
    source_quality = BASE_SCORES.get(event.source_type, 45)
    source_lower = event.source.lower()
    if any(token in source_lower for token in ("ops", "superstella", "byreal", "mantle")):
        source_quality += 20
    mantle_relevance = 40 + min(50, 10 * sum(token in text for token in ("mantle", "mnta", "mainnet", "erc8004", "devhub", "deployment")))
    if event.source_type in {"criteria", "devhub", "mantlescan"}:
        mantle_relevance = max(mantle_relevance, 85)
        source_quality = max(source_quality, 85)
    investment_utility = 35 + min(55, 11 * sum(token in text for token in ("investment", "alpha", "risk", "depeg", "smart money", "vc", "prize", "winner", "deployment")))
    urgency = 35 + min(55, 11 * sum(token in text for token in ("jun 15", "deadline", "delayed", "mainnet", "deployment", "winner")))
    novelty = 35 + min(55, 11 * sum(token in text for token in ("unique", "novel", "registry", "not easily replicate", "early", "verifiable", "mainnet", "deployment")))
    return {
        "source_quality": min(source_quality, 100),
        "mantle_relevance": min(mantle_relevance, 100),
        "investment_utility": min(investment_utility, 100),
        "urgency": min(urgency, 100),
        "novelty": min(novelty, 100),
    }


def build_signal(event: SourceEvent) -> Signal:
    scores = score_event(event)
    confidence = round(
        0.25 * scores["source_quality"]
        + 0.25 * scores["mantle_relevance"]
        + 0.2 * scores["investment_utility"]
        + 0.15 * scores["urgency"]
        + 0.15 * scores["novelty"]
    )
    signal_type = classify(event)
    return Signal(
        id=stable_id(event.id, event.title),
        signal_type=signal_type,
        title=event.title,
        summary=event.text,
        action=recommended_action(signal_type, event),
        confidence=confidence,
        scores=scores,
        source_event_ids=[event.id],
        evidence=[
            {
                "source": event.source,
                "type": event.source_type,
                "url": event.url,
                "observed_at": event.observed_at,
                "excerpt": event.text[:220],
            }
        ],
        tags=event.tags,
        judge_packet=build_judge_packet(signal_type, event, scores, confidence),
    )


def recommended_action(signal_type: str, event: SourceEvent) -> str:
    text = " ".join([event.title, event.text]).lower()
    if "mainnet" in text and "deployment" in text:
        return "Deploy the signal registry on Mantle mainnet before submission to qualify for finalist deployment upside."
    if "criteria" in event.tags or event.source_type == "criteria":
        return "Shape the demo around investor-grade insights, unique Mantle-native data, and verifiable evidence."
    if signal_type == "competitor":
        return "Differentiate the pitch against this competitor and avoid a crowded RWA-vault/backtest framing."
    if signal_type == "risk":
        return "Convert this into an alert rule with evidence, severity, and a recommended investor response."
    if signal_type == "deadline":
        return "Treat as an execution constraint and update the submission checklist."
    return "Promote to the dashboard if corroborated by a second source or a Mantle-native on-chain trace."


def build_judge_packet(signal_type: str, event: SourceEvent, scores: dict[str, int], confidence: int) -> dict[str, str]:
    strongest = sorted(scores.items(), key=lambda item: item[1], reverse=True)[:2]
    strongest_text = ", ".join(f"{name.replace('_', ' ')} {value}" for name, value in strongest)
    source_note = f"{event.source} observed at {event.observed_at}"
    if signal_type == "deadline":
        why_now = "This can change submission priority before judging closes."
        judge_fit = "Shows execution awareness, prize-path mapping, and deadline-driven prioritization."
    elif signal_type == "alpha":
        why_now = "This maps judging criteria into product behavior instead of a generic AI summary."
        judge_fit = "Directly targets Insight value, Data source quality, Investment utility, and Scalability."
    elif signal_type == "risk":
        why_now = "Risk signals are useful before they become obvious in public dashboards."
        judge_fit = "Demonstrates investor utility and a path toward alerting or portfolio monitoring."
    elif signal_type == "competitor":
        why_now = "Competitor signals help position the project away from crowded narratives."
        judge_fit = "Shows market awareness and a practical differentiation loop."
    else:
        why_now = "Mantle ecosystem context is moving quickly and can create short-lived opportunities."
        judge_fit = "Shows Mantle-native relevance with source-backed reasoning."

    return {
        "why_now": why_now,
        "judge_fit": judge_fit,
        "investor_use": f"Confidence {confidence}% from {strongest_text}; source: {source_note}.",
        "risk": "Single-source signals should be promoted only after corroboration or on-chain verification.",
        "proof": "Hash-ready for SignalRegistry commitment on Mantle mainnet.",
    }


def rank_signals(events: Iterable[SourceEvent]) -> list[Signal]:
    signals = [build_signal(event) for event in events]
    return sorted(signals, key=lambda s: (s.confidence, max(s.scores.values())), reverse=True)
