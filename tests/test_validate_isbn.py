import pytest
from src.library import validate_isbn


def test_valid_13_digit_isbn():
    assert validate_isbn("9780132350884") is True


def test_empty_isbn():
    with pytest.raises(ValueError):
        validate_isbn("")


def test_too_short_isbn():
    with pytest.raises(ValueError):
        validate_isbn("123456789")


def test_isbn_with_letters_or_symbols():
    with pytest.raises(ValueError):
        validate_isbn("9780132350ABC")