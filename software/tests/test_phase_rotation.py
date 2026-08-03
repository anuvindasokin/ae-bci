import numpy as np
import pytest
from ae_bci.signal_processing.baseline_subtraction import subtract_xy_offset
from ae_bci.signal_processing.phase_rotation import rotate_lockin_xy


def test_phase_rotation_and_offset():
    recovered = rotate_lockin_xy([2, 3], [4, 5], np.pi / 2, x_offset=1, y_offset=2)
    assert recovered == pytest.approx([2, 3])


def test_offset_subtraction():
    x, y = subtract_xy_offset([2, 3], [4, 5], 1, 2)
    assert x.tolist() == [1, 2]
    assert y.tolist() == [2, 3]


def test_shape_mismatch():
    with pytest.raises(ValueError):
        rotate_lockin_xy([1], [1, 2], 0)

