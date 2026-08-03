"""Pressure normalisation."""

import numpy as np
from numpy.typing import ArrayLike, NDArray


def normalise_by_pressure(
    values: ArrayLike, pressure_pa: ArrayLike
) -> NDArray[np.float64]:
    """Normalise response by calibrated acoustic pressure in pascals."""
    response = np.asarray(values, dtype=float)
    pressure = np.asarray(pressure_pa, dtype=float)
    if np.any(pressure <= 0):
        raise ValueError("Pressure must be positive.")
    try:
        return np.asarray(response / pressure, dtype=float)
    except ValueError as error:
        raise ValueError("Response and pressure are not broadcast-compatible.") from error

