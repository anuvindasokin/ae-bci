"""Validate a one-column waveform CSV against 10 Hz–8 kHz."""

import argparse

import pandas as pd
from ae_bci.signal_processing.filtering import validate_waveform_bandwidth

parser = argparse.ArgumentParser()
parser.add_argument("csv")
parser.add_argument("--sample-rate-hz", type=float, required=True)
args = parser.parse_args()
frame = pd.read_csv(args.csv)
validate_waveform_bandwidth(frame.iloc[:, 0], args.sample_rate_hz)
print("valid")

