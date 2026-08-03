import numpy as np
import pytest
from ae_bci.signal_processing.filtering import validate_waveform_bandwidth


def tone(frequency, sample_rate=40_000, duration=1):
    time = np.arange(int(sample_rate * duration)) / sample_rate
    return np.sin(2 * np.pi * frequency * time)


@pytest.mark.parametrize("frequency", [10, 100, 1_000, 8_000])
def test_supported_tones(frequency):
    validate_waveform_bandwidth(tone(frequency), 40_000)


@pytest.mark.parametrize("frequency", [5, 9_000])
def test_out_of_band_tones(frequency):
    with pytest.raises(ValueError):
        validate_waveform_bandwidth(tone(frequency), 40_000)

