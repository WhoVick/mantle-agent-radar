from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class SourceEvent:
    id: str
    source: str
    source_type: str
    title: str
    text: str
    url: str
    observed_at: str
    tags: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Signal:
    id: str
    signal_type: str
    title: str
    summary: str
    action: str
    confidence: int
    scores: dict[str, int]
    source_event_ids: list[str]
    evidence: list[dict[str, str]]
    tags: list[str]
    judge_packet: dict[str, str] = field(default_factory=dict)
