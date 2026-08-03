"""Count predefined-prominence peaks in a CSV response profile."""

import argparse

import pandas as pd
from ae_bci.analysis.resolution import count_resolved_peaks

parser = argparse.ArgumentParser()
parser.add_argument("csv")
parser.add_argument("--minimum-prominence", type=float, required=True)
args = parser.parse_args()
frame = pd.read_csv(args.csv)
print(
    count_resolved_peaks(
        frame["response_v"], minimum_prominence=args.minimum_prominence
    )
)
