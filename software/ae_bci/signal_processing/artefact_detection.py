"""Basic control-condition artefact screening."""

from collections.abc import Mapping


def detect_control_artefacts(
    amplitudes: Mapping[str, float], *, reduction_ratio: float = 0.25
) -> list[str]:
    """Flag control responses inconsistent with a candidate AE interpretation."""
    required = {"combined", "source_only", "ultrasound_only", "acoustic_blocked", "dummy_load"}
    missing = required - amplitudes.keys()
    if missing:
        raise ValueError(f"Missing control conditions: {sorted(missing)}")
    combined = abs(amplitudes["combined"])
    if combined == 0:
        return ["combined response is zero"]
    return [
        f"{condition} response exceeds control threshold"
        for condition in required - {"combined"}
        if abs(amplitudes[condition]) > reduction_ratio * combined
    ]

