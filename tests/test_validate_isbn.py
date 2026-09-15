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


@pytest.mark.parametrize("length,should_raise", [
    (11, True),
    (12, True),
    (13, False),
    (14, True),
    (15, True),
])
def test_isbn_length_boundaries(length, should_raise):
    isbn = "1" * length

    if should_raise:
        with pytest.raises(ValueError):
            validate_isbn(isbn)
    else:
        assert validate_isbn(isbn) is True