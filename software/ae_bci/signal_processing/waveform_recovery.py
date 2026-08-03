"""Waveform recovery helpers."""

import numpy as np
from numpy.typing import ArrayLike


def waveform_correlation(reference: ArrayLike, recovered: ArrayLike) -> float:
    """Return Pearson correlation between equal-length waveforms."""
    reference_array = np.asarray(reference, dtype=float)
    recovered_array = np.asarray(recovered, dtype=float)
    if reference_array.shape != recovered_array.shape or reference_array.size < 2:
        raise ValueError("Waveforms must have the same shape and at least two samples.")
    if np.std(reference_array) == 0 or np.std(recovered_array) == 0:
        raise ValueError("Waveforms must have non-zero variance.")
    return float(np.corrcoef(reference_array, recovered_array)[0, 1])

