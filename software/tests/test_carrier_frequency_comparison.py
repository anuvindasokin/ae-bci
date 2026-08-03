import pytest
from ae_bci.analysis.frequency_comparison import compare_carrier_configuration


def complete_metrics():
    return {
        "carrier_frequency_hz": 500_000,
        "ae_snr_db": 20,
        "repeatability": 0.9,
        "focal_volume_m3": 1e-9,
        "temperature_rise_k": 0.1,
        "rf_power_w": 1,
        "localisation_error_m": 0.001,
        "carrier_artefact_ratio": 0.1,
        "skull_insertion_loss_db": 10,
    }


def test_comparison_metric():
    assert compare_carrier_configuration(complete_metrics()) > 0


def test_rejects_missing_fields():
    metrics = complete_metrics()
    del metrics["temperature_rise_k"]
    with pytest.raises(ValueError, match="temperature_rise_k"):
        compare_carrier_configuration(metrics)

