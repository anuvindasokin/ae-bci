"""Export a spatial point plot from CSV without overwriting."""

import argparse

import pandas as pd
from ae_bci.visualisation.report_figures import export_figure
from ae_bci.visualisation.spatial_plots import plot_spatial_points

parser = argparse.ArgumentParser()
parser.add_argument("csv")
parser.add_argument("output")
args = parser.parse_args()
frame = pd.read_csv(args.csv)
figure = plot_spatial_points(frame["x_m"], frame["y_m"], frame["response_v"])
print(export_figure(figure, args.output))

