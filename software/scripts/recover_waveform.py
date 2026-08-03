"""Alias for signed X/Y waveform recovery."""

from pathlib import Path
from runpy import run_path

run_path(str(Path(__file__).with_name("analyse_lockin_data.py")), run_name="__main__")

