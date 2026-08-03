"""Linearity regression."""

from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike
from scipy.stats import linregress


@dataclass(frozen=True)
class LinearityResult:
    """Linear regression result."""

    slope: float
    intercept: float
    r_squared: float
    p_value: float
    standard_error: float


def fit_linearity(independent: ArrayLike, response: ArrayLike) -> LinearityResult:
    """Fit response against an experimental independent variable."""
    x = np.asarray(independent, dtype=float)
    y = np.asarray(response, dtype=float)
    if x.ndim != 1 or x.shape != y.shape or x.size < 3:
        raise ValueError("At least three paired 1D observations are required.")
    result = linregress(x, y)
    return LinearityResult(
        float(result.slope),
        float(result.intercept),
        float(result.rvalue**2),
        float(result.pvalue),
        float(result.stderr),
    )

