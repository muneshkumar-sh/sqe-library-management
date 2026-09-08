import pytest
from src.library import fine_tier


@pytest.mark.parametrize('days,expected', [
    (0, 'None'),
    (4, 'Low'),
    (10, 'Medium'),
    (20, 'High'),
    (45, 'Severe'),
])
def test_fine_tier_valid_classes(days, expected):
    assert fine_tier(days) == expected


def test_fine_tier_negative_days_raises():
    with pytest.raises(ValueError):
        fine_tier(-3)