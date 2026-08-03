"""Fit response against measured source current from CSV."""

import argparse
from dataclasses import asdict
import json
import pandas as pd
from ae_bci.analysis.linearity import fit_linearity

parser = argparse.ArgumentParser()
parser.add_argument("csv")
args = parser.parse_args()
frame = pd.read_csv(args.csv)
print(json.dumps(asdict(fit_linearity(frame["source_current_a_rms"], frame["response_v"])), indent=2))

