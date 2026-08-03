"""Two-source resolution utilities."""

import numpy as np
from numpy.typing import ArrayLike
from scipy.signal import find_peaks


def count_resolved_peaks(profile: ArrayLike, *, minimum_prominence: float) -> int:
    """Count peaks meeting a predefined prominence criterion."""
    values = np.asarray(profile, dtype=float)
    if values.ndim != 1 or values.size < 3 or minimum_prominence <= 0:
        raise ValueError("A 1D profile and positive prominence are required.")
    peaks, _ = find_peaks(values, prominence=minimum_prominence)
    return int(peaks.size)

