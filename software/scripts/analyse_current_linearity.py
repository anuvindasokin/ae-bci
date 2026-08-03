"""Fit response against measured source current from CSV."""

import argparse
import json
from dataclasses import asdict

import pandas as pd
from ae_bci.analysis.linearity import fit_linearity

parser = argparse.ArgumentParser()
parser.add_argument("csv")
args = parser.parse_args()
frame = pd.read_csv(args.csv)
result = fit_linearity(frame["source_current_a_rms"], frame["response_v"])
print(json.dumps(asdict(result), indent=2))
