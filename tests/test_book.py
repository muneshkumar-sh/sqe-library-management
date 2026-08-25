import pytest
from src.book import Book


def test_empty_isbn_is_rejected():
    with pytest.raises(ValueError, match="ISBN cannot be empty"):
        Book("", "Clean Code", "Robert C. Martin")


def test_whitespace_isbn_is_rejected():
    with pytest.raises(ValueError, match="ISBN cannot be empty"):
        Book("   ", "Clean Code", "Robert C. Martin")


def test_valid_isbn_is_accepted():
    book = Book("9780132350884", "Clean Code", "Robert C. Martin")
    assert book.isbn == "9780132350884"