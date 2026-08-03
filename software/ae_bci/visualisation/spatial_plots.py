"""Spatial plotting helpers."""

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from numpy.typing import ArrayLike


def plot_spatial_points(x_m: ArrayLike, y_m: ArrayLike, values: ArrayLike) -> Figure:
    """Create a metric-coordinate coloured point map."""
    figure, axis = plt.subplots()
    scatter = axis.scatter(x_m, y_m, c=values)
    axis.set(xlabel="x (m)", ylabel="y (m)", title="Spatial scan")
    figure.colorbar(scatter, ax=axis, label="Response (SI unit documented by caller)")
    return figure

