import pytest
from src.library import Library


@pytest.mark.parametrize(
    "current_books, should_raise",
    [
        (0, False),
        (1, False),
        (2, False),
        (3, False),
        (4, False),
        (5, True),
    ],
    ids=[
        "empty-member-can-borrow",
        "one-book-can-borrow",
        "two-books-can-borrow",
        "three-books-can-borrow",
        "four-books-can-borrow",
        "five-books-at-limit",
    ],
)
def test_borrow_book_edge_cases(current_books, should_raise):
    # Arrange
    library = Library()
    member_id = "M001"

    for i in range(current_books):
        library.borrow_book(member_id, f"ISBN{i}")

    # Act & Assert
    if should_raise:
        with pytest.raises(ValueError, match="Borrow limit exceeded"):
            library.borrow_book(member_id, "ISBN_NEW")
    else:
        library.borrow_book(member_id, "ISBN_NEW")
        assert len(library.loans[member_id]) == current_books + 1