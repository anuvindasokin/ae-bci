"""Calculate linear response from CSV input/output amplitude columns."""

import argparse

import pandas as pd
from ae_bci.signal_processing.frequency_response import calculate_frequency_response

parser = argparse.ArgumentParser()
parser.add_argument("csv")
args = parser.parse_args()
frame = pd.read_csv(args.csv)
frame["linear_gain"] = calculate_frequency_response(
    frame["output_amplitude"], frame["input_amplitude"]
)
print(frame.to_csv(index=False))
