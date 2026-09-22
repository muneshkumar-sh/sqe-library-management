import pytest
from src.book import Book


# Function-scoped fixture:
# A new Book object is created for every test.
# This is appropriate when tests modify the object and must remain independent.
@pytest.fixture
def valid_book():
    return Book("9780132350884", "Clean Code", "Robert C. Martin")


# Module-scoped fixture:
# This setup is created once for the whole test module.
# It is appropriate for expensive, read-only setup that can safely be shared.
@pytest.fixture(scope="module")
def book_catalog():
    return [
        Book("9780132350884", "Clean Code", "Robert C. Martin"),
        Book("9780135957059", "The Pragmatic Programmer", "Andrew Hunt"),
    ]


def test_empty_isbn_is_rejected():
    with pytest.raises(ValueError, match="ISBN cannot be empty"):
        Book("", "Clean Code", "Robert C. Martin")


def test_whitespace_isbn_is_rejected():
    with pytest.raises(ValueError, match="ISBN cannot be empty"):
        Book("   ", "Clean Code", "Robert C. Martin")


def test_non_numeric_rating_is_rejected(valid_book):
    with pytest.raises(
        ValueError,
        match="Rating must be a number between 0 and 5"
    ):
        valid_book.add_rating("five")


def test_valid_rating_is_accepted(valid_book):
    valid_book.add_rating(4)

    assert valid_book.rating == 4


def test_rating_above_maximum_is_rejected(valid_book):
    with pytest.raises(ValueError, match="Rating must be between 0 and 5"):
        valid_book.add_rating(6)


def test_empty_title_is_rejected():
    with pytest.raises(ValueError, match="Book title cannot be empty"):
        Book("9780132350884", "", "Robert C. Martin")


def test_whitespace_title_is_rejected():
    with pytest.raises(ValueError, match="Book title cannot be empty"):
        Book("9780132350884", "   ", "Robert C. Martin")


def test_valid_title_is_accepted(book_catalog):
    assert book_catalog[0].title == "Clean Code"


def test_none_isbn_is_rejected():
    with pytest.raises(ValueError, match="ISBN cannot be empty"):
        Book(None, "Clean Code", "Robert C. Martin")