"""Waveform bandwidth validation."""

import numpy as np
from numpy.typing import ArrayLike


def validate_waveform_bandwidth(
    samples: ArrayLike,
    sample_rate_hz: float,
    *,
    minimum_hz: float = 10.0,
    maximum_hz: float = 8_000.0,
    relative_threshold: float = 1e-6,
) -> None:
    """Raise when material spectral energy lies outside the supported band."""
    values = np.asarray(samples, dtype=float)
    if values.ndim != 1 or values.size < 2:
        raise ValueError("Samples must be a 1D array with at least two values.")
    if sample_rate_hz <= 2 * maximum_hz:
        raise ValueError("Sample rate must exceed twice the maximum frequency.")
    spectrum = np.abs(np.fft.rfft(values - np.mean(values)))
    frequencies = np.fft.rfftfreq(values.size, 1 / sample_rate_hz)
    peak = float(np.max(spectrum))
    if peak == 0:
        raise ValueError("Waveform has no AC content.")
    outside = (frequencies < minimum_hz) | (frequencies > maximum_hz)
    if np.any(spectrum[outside] > peak * relative_threshold):
        raise ValueError("Waveform contains material content outside 10 Hz to 8 kHz.")

