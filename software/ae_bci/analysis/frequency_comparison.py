"""Carrier-frequency engineering comparison."""

from collections.abc import Mapping

REQUIRED_METRICS = {
    "carrier_frequency_hz",
    "ae_snr_db",
    "repeatability",
    "focal_volume_m3",
    "temperature_rise_k",
    "rf_power_w",
    "localisation_error_m",
    "carrier_artefact_ratio",
    "skull_insertion_loss_db",
}


def compare_carrier_configuration(metrics: Mapping[str, float]) -> float:
    """Return the optional unweighted Q metric after completeness checks.

    Q is an engineering comparison aid, not a biological safety limit. Individual
    measurements must always remain visible alongside this score.
    """
    missing = REQUIRED_METRICS - metrics.keys()
    if missing:
        raise ValueError(f"Missing required comparison fields: {sorted(missing)}")
    positive = ("repeatability", "focal_volume_m3", "temperature_rise_k", "rf_power_w")
    if any(metrics[name] <= 0 for name in positive):
        raise ValueError("Repeatability and denominator metrics must be positive.")
    linear_snr = 10 ** (metrics["ae_snr_db"] / 20)
    return float(
        linear_snr
        * metrics["repeatability"]
        / (
            metrics["focal_volume_m3"]
            * metrics["temperature_rise_k"]
            * metrics["rf_power_w"]
        )
    )

