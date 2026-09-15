import pytest
from src.library import fine_tier


@pytest.mark.parametrize("days,expected", [
    (-1, "ValueError"),
    (0, "None"),
    (1, "Low"),
    (2, "Low"),
    (7, "Low"),
    (8, "Medium"),
    (9, "Medium"),
    (14, "Medium"),
    (15, "High"),
    (16, "High"),
    (30, "High"),
    (31, "Severe"),
    (32, "Severe"),
])
def test_fine_tier_boundaries(days, expected):
    if expected == "ValueError":
        with pytest.raises(ValueError):
            fine_tier(days)
    else:
        assert fine_tier(days) == expected