import pytest
from src.library import Library


@pytest.mark.parametrize('current_books,should_raise', [
    (3, False),
    (5, True),
])
def test_borrow_limit(current_books, should_raise):
    library = Library()
    member_id = "M001"

    for i in range(current_books):
        library.borrow_book(member_id, f"ISBN{i}")

    if should_raise:
        with pytest.raises(ValueError):
            library.borrow_book(member_id, "ISBN_NEW")
    else:
        library.borrow_book(member_id, "ISBN_NEW")
        assert library.loans[member_id] == current_books + 1