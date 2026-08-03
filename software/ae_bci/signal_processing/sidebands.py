"""Acoustoelectric heterodyne sideband calculations."""


def calculate_sidebands(
    carrier_frequency_hz: float,
    source_frequency_hz: float,
) -> tuple[float, float]:
    """Return lower and upper heterodyne sideband frequencies in hertz."""
    if carrier_frequency_hz <= 0:
        raise ValueError("Carrier frequency must be positive.")
    if source_frequency_hz < 0:
        raise ValueError("Source frequency cannot be negative.")
    if source_frequency_hz >= carrier_frequency_hz:
        raise ValueError("Source frequency must be lower than carrier frequency.")
    return (
        carrier_frequency_hz - source_frequency_hz,
        carrier_frequency_hz + source_frequency_hz,
    )

