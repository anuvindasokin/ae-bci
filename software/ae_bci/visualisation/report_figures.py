"""Figure export with explicit paths."""

from pathlib import Path

from matplotlib.figure import Figure


def export_figure(figure: Figure, path: str | Path, *, dpi: int = 300) -> Path:
    """Export a figure, refusing to overwrite an existing result silently."""
    output = Path(path)
    if output.exists():
        raise FileExistsError(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output, dpi=dpi, bbox_inches="tight")
    return output

