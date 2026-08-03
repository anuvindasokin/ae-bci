import pytest

from ae_bci.signal_processing.sidebands import calculate_sidebands


@pytest.mark.parametrize(
    ("carrier", "source", "expected"),
    [
        (500_000, 10, (499_990, 500_010)),
        (500_000, 8_000, (492_000, 508_000)),
        (650_000, 8_000, (642_000, 658_000)),
        (750_000, 8_000, (742_000, 758_000)),
        (1_000_000, 8_000, (992_000, 1_008_000)),
        (823_456, 1_234, (822_222, 824_690)),
    ],
)
def test_sidebands(carrier, source, expected):
    assert calculate_sidebands(carrier, source) == expected


@pytest.mark.parametrize("carrier,source", [(-1, 10), (500_000, -1), (100, 100), (100, 101)])
def test_invalid_frequencies(carrier, source):
    with pytest.raises(ValueError):
        calculate_sidebands(carrier, source)

