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

def test_borrow_limit_boundaries():
    library = Library()
    member_id = "M001"

    # Boundary: 4 books -> borrowing one more should be allowed
    for i in range(4):
        library.borrow_book(member_id, f"ISBN{i}")

    library.borrow_book(member_id, "ISBN4")
    assert library.loans[member_id] == 5

    # Boundary: 5 books -> borrowing one more should be rejected
    with pytest.raises(ValueError):
        library.borrow_book(member_id, "ISBN5")

    # Boundary: 6 books -> system should not allow 6 books
    assert library.loans[member_id] == 5