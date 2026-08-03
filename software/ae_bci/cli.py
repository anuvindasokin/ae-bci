"""Small command-line entry points."""

import argparse

from ae_bci.io.metadata import load_metadata
from ae_bci.signal_processing.sidebands import calculate_sidebands


def sidebands_main() -> None:
    """Calculate a lower and upper sideband from command-line values."""
    parser = argparse.ArgumentParser()
    parser.add_argument("carrier_frequency_hz", type=float)
    parser.add_argument("source_frequency_hz", type=float)
    args = parser.parse_args()
    lower, upper = calculate_sidebands(
        args.carrier_frequency_hz, args.source_frequency_hz
    )
    print(f"lower_hz={lower:g}\nupper_hz={upper:g}")


def validate_main() -> None:
    """Validate an experiment metadata file."""
    parser = argparse.ArgumentParser()
    parser.add_argument("metadata")
    args = parser.parse_args()
    metadata = load_metadata(args.metadata)
    print(f"valid experiment_id={metadata.experiment_id}")
