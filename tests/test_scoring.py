from agent_radar.models import SourceEvent
from agent_radar.scoring import build_signal


def test_mantle_mainnet_deployment_signal_scores_high():
    event = SourceEvent(
        id="event-1",
        source="Telegram / Ops",
        source_type="telegram",
        title="Mainnet deployment is preferred",
        text="Mantle mainnet deployment counts better for final winner selection.",
        url="https://example.com",
        observed_at="2026-06-08T00:00:00Z",
        tags=["mantle", "mainnet", "deployment", "winner"],
    )
    signal = build_signal(event)
    assert signal.confidence >= 65
    assert signal.signal_type in {"ecosystem", "deadline"}
    assert "Deploy" in signal.action

