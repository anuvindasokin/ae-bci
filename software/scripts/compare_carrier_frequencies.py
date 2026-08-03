"""Calculate a complete carrier-configuration engineering metric from JSON."""

import argparse
import json
from pathlib import Path

from ae_bci.analysis.frequency_comparison import compare_carrier_configuration

parser = argparse.ArgumentParser()
parser.add_argument("metrics_json")
args = parser.parse_args()
metrics = json.loads(Path(args.metrics_json).read_text(encoding="utf-8"))
print(compare_carrier_configuration(metrics))

