from datetime import date

import pytest
from ae_bci.io.metadata import ExperimentMetadata
from pydantic import ValidationError


def valid_metadata():
    return {
        "schema_version": "1.0",
        "experiment_id": "AE-001",
        "acquisition_date": date(2026, 1, 1),
        "acquisition_git_commit": "abcdef1",
        "dataset_type": "synthetic",
        "carrier_frequency_hz": 500_000,
        "lockin_reference_frequency_hz": 500_000,
        "source_frequency_hz": 1_000,
        "source_waveform": "sine",
        "source_id": "SRC-X-001",
        "source_current_a_rms": 1e-6,
        "receiver_id": "RX-001",
        "ultrasound_configuration_id": "US-500-TBD",
        "controls": ["baseline", "source_only", "ultrasound_only", "combined"],
        "calibration_references": {
            "source_current": "CAL-SRC-001",
            "receiver_transfer_function": "CAL-RX-001",
            "transducer_pressure": "CAL-US-001",
            "lockin": "CAL-LI-001",
        },
        "operator": "test",
    }


def test_valid_metadata():
    assert ExperimentMetadata.model_validate(valid_metadata()).experiment_id == "AE-001"


def test_lockin_reference_mismatch():
    values = valid_metadata()
    values["lockin_reference_frequency_hz"] = 650_000
    with pytest.raises(ValidationError, match="does not match"):
        ExperimentMetadata.model_validate(values)


def test_source_bandwidth():
    values = valid_metadata()
    values["source_frequency_hz"] = 8_001
    with pytest.raises(ValidationError):
        ExperimentMetadata.model_validate(values)


def test_missing_calibration():
    values = valid_metadata()
    del values["calibration_references"]["lockin"]
    with pytest.raises(ValidationError):
        ExperimentMetadata.model_validate(values)

