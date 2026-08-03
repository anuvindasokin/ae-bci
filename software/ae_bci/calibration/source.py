"""Source-current normalisation."""

import numpy as np
from numpy.typing import ArrayLike, NDArray


def normalise_by_source_current(
    values: ArrayLike, source_current_a_rms: ArrayLike
) -> NDArray[np.float64]:
    """Normalise response by measured RMS source current in amperes."""
    response = np.asarray(values, dtype=float)
    current = np.asarray(source_current_a_rms, dtype=float)
    if np.any(current <= 0):
        raise ValueError("Source current must be positive.")
    try:
        return np.asarray(response / current, dtype=float)
    except ValueError as error:
        raise ValueError("Response and current are not broadcast-compatible.") from error

