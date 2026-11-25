import pytest

from src.library import Library, borrow_percentile


def test_borrow_percentile_with_fewer_books():
    library = Library()
    library.loans["M0"] = []
    library.loans["M1"] = ["BOOK1"]
    library.loans["M2"] = ["BOOK2", "BOOK3"]

    result = borrow_percentile("M1", library)

    assert result == pytest.approx(100 / 3)


def test_borrow_percentile_with_equal_books():
    library = Library()
    library.borrow_book("M1", "BOOK1")
    library.borrow_book("M2", "BOOK2")

    result = borrow_percentile("M1", library)

    assert result == 0.0


def test_borrow_percentile_with_empty_library():
    library = Library()

    with pytest.raises(ValueError, match="empty library"):
        borrow_percentile("M1", library)


def test_borrow_percentile_with_unknown_member():
    library = Library()
    library.borrow_book("M1", "BOOK1")

    with pytest.raises(ValueError, match="Member not found"):
        borrow_percentile("M2", library)


def test_borrow_percentile_with_single_member():
    library = Library()
    library.borrow_book("M1", "BOOK1")

    result = borrow_percentile("M1", library)

    assert result == 0.0