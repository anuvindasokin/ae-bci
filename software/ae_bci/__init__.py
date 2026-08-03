"""AE-BCI analysis and validation utilities."""

from ae_bci.signal_processing.phase_rotation import rotate_lockin_xy
from ae_bci.signal_processing.sidebands import calculate_sidebands

__all__ = ["calculate_sidebands", "rotate_lockin_xy"]
__version__ = "0.1.0"

