"""Spatial scan interpolation."""

import numpy as np
from numpy.typing import ArrayLike, NDArray
from scipy.interpolate import griddata


def interpolate_spatial_scan(
    coordinates_m: ArrayLike,
    values: ArrayLike,
    query_coordinates_m: ArrayLike,
    *,
    method: str = "linear",
) -> NDArray[np.float64]:
    """Interpolate samples while preserving SI-coordinate conventions."""
    coordinates = np.asarray(coordinates_m, dtype=float)
    sample_values = np.asarray(values, dtype=float)
    query = np.asarray(query_coordinates_m, dtype=float)
    if coordinates.ndim != 2 or sample_values.shape != (coordinates.shape[0],):
        raise ValueError("Coordinates must be NxD with one value per coordinate.")
    if query.ndim != 2 or query.shape[1] != coordinates.shape[1]:
        raise ValueError("Query coordinates must use the same dimensionality.")
    if method not in {"nearest", "linear", "cubic"}:
        raise ValueError("Unsupported interpolation method.")
    return np.asarray(griddata(coordinates, sample_values, query, method=method))

