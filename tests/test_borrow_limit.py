import pytest
from src.library import Library


# Function-scoped fixture:
# A fresh Library is created for every test so that loans from one
# test cannot affect another test.
@pytest.fixture
def library():
    return Library()


@pytest.mark.parametrize(
    "current_books,should_raise",
    [
        (3, False),
        (5, True),
    ],
)
def test_borrow_limit(library, current_books, should_raise):
    member_id = "M001"

    for i in range(current_books):
        library.borrow_book(member_id, f"ISBN{i}")

    if should_raise:
        with pytest.raises(ValueError):
            library.borrow_book(member_id, "ISBN_NEW")
    else:
        library.borrow_book(member_id, "ISBN_NEW")
        assert len(library.loans[member_id]) == current_books + 1


def test_borrow_limit_boundaries(library):
    member_id = "M001"

    # Boundary: 4 books -> borrowing one more should be allowed
    for i in range(4):
        library.borrow_book(member_id, f"ISBN{i}")

    library.borrow_book(member_id, "ISBN4")
    assert len(library.loans[member_id]) == 5

    # Boundary: 5 books -> borrowing one more should be rejected
    with pytest.raises(ValueError):
        library.borrow_book(member_id, "ISBN5")

    # The member must still have exactly 5 books
    assert len(library.loans[member_id]) == 5


def test_borrow_book_tracks_isbn(library):
    member_id = "M001"
    isbn = "9780132350884"

    library.borrow_book(member_id, isbn)

    assert library.loans[member_id] == [isbn]