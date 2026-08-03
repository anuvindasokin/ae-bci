"""Generate a provenance-first Markdown metadata summary."""

import argparse
from pathlib import Path

from ae_bci.io.metadata import load_metadata

parser = argparse.ArgumentParser()
parser.add_argument("metadata")
parser.add_argument("output")
args = parser.parse_args()
metadata = load_metadata(args.metadata)
output = Path(args.output)
if output.exists():
    raise FileExistsError(output)
output.write_text(
    f"# Experiment {metadata.experiment_id}\n\n"
    f"- Dataset type: {metadata.dataset_type}\n"
    f"- Carrier: {metadata.carrier_frequency_hz:g} Hz\n"
    f"- Source: {metadata.source_frequency_hz:g} Hz ({metadata.source_waveform})\n"
    f"- Acquisition commit: `{metadata.acquisition_git_commit}`\n"
    "\n> No physical interpretation is generated automatically.\n",
    encoding="utf-8",
)
print(output)

