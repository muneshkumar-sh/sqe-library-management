import pytest
from src.library import Library
from src.book import Book


@pytest.fixture
def populated_library():
    library = Library()

    book1 = Book(
        "9780132350884",
        "Clean Code",
        "Robert C. Martin",
        total_copies=2
    )

    book2 = Book(
        "9780135957059",
        "The Pragmatic Programmer",
        "Andrew Hunt",
        total_copies=3
    )

    library.add_book(book1)
    library.add_book(book2)

    return library


def test_total_available_copies_empty():
    # Arrange
    library = Library()

    # Act
    result = library.total_available_copies()

    # Assert
    assert result == 0


def test_total_available_copies_single_book():
    # Arrange
    library = Library()

    book = Book(
        "9780132350884",
        "Clean Code",
        "Robert C. Martin",
        total_copies=2
    )

    library.add_book(book)

    # Act
    result = library.total_available_copies()

    # Assert
    assert result == 2


def test_total_available_copies_multiple_books(populated_library):
    # Act
    result = populated_library.total_available_copies()

    # Assert
    assert result == 5