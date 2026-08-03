"""Frequency-response plotting."""

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from numpy.typing import ArrayLike


def plot_frequency_response(frequency_hz: ArrayLike, gain: ArrayLike) -> Figure:
    """Create a labelled logarithmic-frequency gain figure."""
    figure, axis = plt.subplots()
    axis.semilogx(frequency_hz, gain)
    axis.set(xlabel="Frequency (Hz)", ylabel="Linear gain", title="Frequency response")
    axis.grid(True, which="both")
    return figure

