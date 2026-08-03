"""Experiment metadata schema and loading."""

from datetime import date
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field, model_validator


class CalibrationReferences(BaseModel):
    """Required calibration record identifiers."""

    model_config = ConfigDict(extra="forbid")
    source_current: str = Field(min_length=1)
    receiver_transfer_function: str = Field(min_length=1)
    transducer_pressure: str = Field(min_length=1)
    lockin: str = Field(min_length=1)


class ExperimentMetadata(BaseModel):
    """Minimum reproducibility metadata for an AE-BCI acquisition."""

    model_config = ConfigDict(extra="forbid")
    schema_version: Literal["1.0"]
    experiment_id: str = Field(pattern=r"^[A-Za-z0-9][A-Za-z0-9._-]+$")
    acquisition_date: date
    acquisition_git_commit: str = Field(pattern=r"^[0-9a-fA-F]{7,40}$")
    dataset_type: Literal["measurement", "synthetic", "simulation"]
    carrier_frequency_hz: float = Field(gt=0)
    lockin_reference_frequency_hz: float = Field(gt=0)
    source_frequency_hz: float = Field(ge=10, le=8_000)
    source_waveform: str = Field(min_length=1)
    source_id: str = Field(min_length=1)
    source_current_a_rms: float = Field(gt=0)
    receiver_id: str = Field(min_length=1)
    ultrasound_configuration_id: str = Field(min_length=1)
    controls: list[str] = Field(min_length=1)
    calibration_references: CalibrationReferences
    operator: str = Field(min_length=1)
    notes: str = ""

    @model_validator(mode="after")
    def reference_matches_carrier(self) -> "ExperimentMetadata":
        """Require a coherent lock-in reference at the selected carrier."""
        tolerance_hz = max(0.1, self.carrier_frequency_hz * 1e-6)
        if abs(self.lockin_reference_frequency_hz - self.carrier_frequency_hz) > tolerance_hz:
            raise ValueError("Lock-in reference does not match carrier frequency.")
        if self.source_frequency_hz >= self.carrier_frequency_hz:
            raise ValueError("Source frequency must be lower than carrier frequency.")
        return self


def load_metadata(path: str | Path) -> ExperimentMetadata:
    """Load and validate an experiment metadata YAML mapping."""
    metadata_path = Path(path)
    if not metadata_path.is_file():
        raise FileNotFoundError(f"Metadata file not found: {metadata_path}")
    with metadata_path.open(encoding="utf-8") as stream:
        raw = yaml.safe_load(stream)
    if not isinstance(raw, dict):
        raise ValueError("Metadata document must contain a YAML mapping.")
    return ExperimentMetadata.model_validate(raw)

