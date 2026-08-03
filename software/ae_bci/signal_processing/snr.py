"""Signal-to-noise estimation."""

import numpy as np
from numpy.typing import ArrayLike


def estimate_snr_db(signal: ArrayLike, noise: ArrayLike) -> float:
    """Estimate RMS amplitude SNR in decibels."""
    signal_array = np.asarray(signal, dtype=float)
    noise_array = np.asarray(noise, dtype=float)
    if signal_array.size == 0 or noise_array.size == 0:
        raise ValueError("Signal and noise arrays cannot be empty.")
    noise_rms = np.sqrt(np.mean(np.square(noise_array)))
    if noise_rms == 0:
        raise ValueError("Noise RMS cannot be zero.")
    signal_rms = np.sqrt(np.mean(np.square(signal_array)))
    return float(20 * np.log10(signal_rms / noise_rms))

