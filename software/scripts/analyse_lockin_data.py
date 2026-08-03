"""Recover signed lock-in voltage from a CSV with x and y columns."""

import argparse

import pandas as pd
from ae_bci.signal_processing.phase_rotation import rotate_lockin_xy

parser = argparse.ArgumentParser()
parser.add_argument("csv")
parser.add_argument("--phase-radians", type=float, required=True)
parser.add_argument("--x-offset", type=float, default=0)
parser.add_argument("--y-offset", type=float, default=0)
args = parser.parse_args()
frame = pd.read_csv(args.csv)
frame["recovered_v"] = rotate_lockin_xy(
    frame["x"], frame["y"], args.phase_radians,
    x_offset=args.x_offset, y_offset=args.y_offset,
)
print(frame.to_csv(index=False))

