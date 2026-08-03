"""Lock-in carrier drift estimation."""

import numpy as np
from numpy.typing import ArrayLike


def estimate_carrier_drift_hz(
    timestamps_s: ArrayLike, carrier_frequency_hz: ArrayLike
) -> float:
    """Return fitted carrier-frequency drift rate in hertz per second."""
    time = np.asarray(timestamps_s, dtype=float)
    frequency = np.asarray(carrier_frequency_hz, dtype=float)
    if time.ndim != 1 or time.shape != frequency.shape or time.size < 2:
        raise ValueError("At least two paired 1D time/frequency samples are required.")
    if np.any(np.diff(time) <= 0):
        raise ValueError("Timestamps must be strictly increasing.")
    slope, _ = np.polyfit(time, frequency, 1)
    return float(slope)

