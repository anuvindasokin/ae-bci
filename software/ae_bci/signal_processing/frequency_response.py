"""Frequency-response and group-delay analysis."""

import numpy as np
from numpy.typing import ArrayLike, NDArray


def calculate_frequency_response(
    output_amplitude: ArrayLike, input_amplitude: ArrayLike
) -> NDArray[np.float64]:
    """Return linear amplitude gain for paired input and output amplitudes."""
    output = np.asarray(output_amplitude, dtype=float)
    input_ = np.asarray(input_amplitude, dtype=float)
    if output.shape != input_.shape:
        raise ValueError("Input and output arrays must have identical shapes.")
    if np.any(input_ == 0):
        raise ValueError("Input amplitude cannot be zero.")
    return output / input_


def estimate_group_delay(frequency_hz: ArrayLike, phase_radians: ArrayLike) -> float:
    """Estimate constant group delay from unwrapped phase by linear regression."""
    frequency = np.asarray(frequency_hz, dtype=float)
    phase = np.asarray(phase_radians, dtype=float)
    if frequency.ndim != 1 or phase.ndim != 1 or frequency.size != phase.size:
        raise ValueError("Frequency and phase must be equal-length 1D arrays.")
    if frequency.size < 2 or np.any(np.diff(frequency) <= 0):
        raise ValueError("At least two strictly increasing frequencies are required.")
    slope, _ = np.polyfit(frequency, np.unwrap(phase), 1)
    return float(-slope / (2 * np.pi))

