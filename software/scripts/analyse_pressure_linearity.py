"""Fit response against calibrated pressure from CSV."""

import argparse
from dataclasses import asdict
import json
import pandas as pd
from ae_bci.analysis.linearity import fit_linearity

parser = argparse.ArgumentParser()
parser.add_argument("csv")
args = parser.parse_args()
frame = pd.read_csv(args.csv)
print(json.dumps(asdict(fit_linearity(frame["pressure_pa"], frame["response_v"])), indent=2))

