from src.library import Library
import src.library as library_module


def test_rank_empty_library_returns_empty_list():
    library = Library()

    result = library_module.rank_books_by_popularity(library)

    assert result == []

from src.book import Book


def test_rank_single_book_returns_that_book():
    library = Library()
    book = Book("9780132350884", "Clean Code", "Robert C. Martin")
    library.add_book(book)

    result = library_module.rank_books_by_popularity(library)

    assert result == [book]

def test_rank_books_by_borrowing_count():
    library = Library()

    book1 = Book("9780132350884", "Clean Code", "Robert C. Martin")
    book2 = Book("9780135957059", "The Pragmatic Programmer", "Andrew Hunt")
    book3 = Book("9780134494166", "Clean Architecture", "Robert C. Martin")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Clean Code: 1 borrowing
    library.borrow_book("M1", book1.isbn)

    # The Pragmatic Programmer: 3 borrowings
    library.borrow_book("M1", book2.isbn)
    library.borrow_book("M2", book2.isbn)
    library.borrow_book("M3", book2.isbn)

    # Clean Architecture: 2 borrowings
    library.borrow_book("M1", book3.isbn)
    library.borrow_book("M2", book3.isbn)

    result = library_module.rank_books_by_popularity(library)

    assert result == [book2, book3, book1]