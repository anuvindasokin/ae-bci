"""Ultrasound-only lock-in offset subtraction."""

import numpy as np
from numpy.typing import ArrayLike, NDArray


def subtract_xy_offset(
    x: ArrayLike, y: ArrayLike, x_offset: float, y_offset: float
) -> tuple[NDArray[np.float64], NDArray[np.float64]]:
    """Subtract measured ultrasound-only X/Y offsets without modifying inputs."""
    x_array = np.asarray(x, dtype=float)
    y_array = np.asarray(y, dtype=float)
    if x_array.shape != y_array.shape:
        raise ValueError("X and Y must have identical shapes.")
    return x_array - x_offset, y_array - y_offset

