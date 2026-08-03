"""Lock-in phase rotation."""

import numpy as np
from numpy.typing import ArrayLike, NDArray


def rotate_lockin_xy(
    x: ArrayLike,
    y: ArrayLike,
    phase_radians: float,
    *,
    x_offset: float = 0.0,
    y_offset: float = 0.0,
) -> NDArray[np.float64]:
    """Recover a signed waveform after offset subtraction and phase rotation."""
    x_array = np.asarray(x, dtype=float)
    y_array = np.asarray(y, dtype=float)
    if x_array.shape != y_array.shape:
        raise ValueError("X and Y must have identical shapes.")
    return (x_array - x_offset) * np.cos(phase_radians) + (
        y_array - y_offset
    ) * np.sin(phase_radians)

