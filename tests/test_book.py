import pytest
from src.book import Book


def test_empty_isbn_is_rejected():
    with pytest.raises(ValueError, match="ISBN cannot be empty"):
        Book("", "Clean Code", "Robert C. Martin")


def test_whitespace_isbn_is_rejected():
    with pytest.raises(ValueError, match="ISBN cannot be empty"):
        Book("   ", "Clean Code", "Robert C. Martin")


def test_non_numeric_rating_is_rejected():
    book = Book("9780132350884", "Clean Code", "Robert C. Martin")

    with pytest.raises(ValueError, match="Rating must be a number between 0 and 5"):
        book.add_rating("five")


def test_valid_rating_is_accepted():
    book = Book("9780132350884", "Clean Code", "Robert C. Martin")

    book.add_rating(4)

    assert book.rating == 4

def test_rating_above_maximum_is_rejected():
    book = Book("9780132350884", "Clean Code", "Robert C. Martin")

    with pytest.raises(ValueError, match="Rating must be between 0 and 5"):
        book.add_rating(6)