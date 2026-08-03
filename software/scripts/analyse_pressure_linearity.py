"""Fit response against calibrated pressure from CSV."""

import argparse
import json
from dataclasses import asdict

import pandas as pd
from ae_bci.analysis.linearity import fit_linearity

parser = argparse.ArgumentParser()
parser.add_argument("csv")
args = parser.parse_args()
frame = pd.read_csv(args.csv)
result = fit_linearity(frame["pressure_pa"], frame["response_v"])
print(json.dumps(asdict(result), indent=2))
