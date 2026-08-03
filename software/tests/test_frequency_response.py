import numpy as np
import pytest
from ae_bci.signal_processing.frequency_response import (
    calculate_frequency_response,
    estimate_group_delay,
)


def test_frequency_response():
    assert calculate_frequency_response([2, 4], [1, 2]).tolist() == [2, 2]


def test_group_delay():
    frequency = np.array([10, 100, 1_000, 8_000])
    delay = 12e-6
    phase = -2 * np.pi * frequency * delay
    assert estimate_group_delay(frequency, phase) == pytest.approx(delay)

