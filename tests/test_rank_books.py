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

def test_equal_borrow_counts_are_sorted_alphabetically():
    library = Library()

    book_z = Book("9780132350884", "Zebra Coding", "Author Z")
    book_a = Book("9780135957059", "Alpha Coding", "Author A")
    book_m = Book("9780134494166", "Middle Coding", "Author M")

    library.add_book(book_z)
    library.add_book(book_a)
    library.add_book(book_m)

    library.borrow_book("M1", book_z.isbn)
    library.borrow_book("M1", book_a.isbn)
    library.borrow_book("M1", book_m.isbn)

    result = library_module.rank_books_by_popularity(library)

    assert result == [book_a, book_m, book_z]

def test_never_borrowed_book_ranks_after_borrowed_books():
    library = Library()

    borrowed_book = Book(
        "9780132350884", "Clean Code", "Robert C. Martin"
    )
    unused_book = Book(
        "9780135957059", "Alpha Coding", "Author A"
    )

    library.add_book(borrowed_book)
    library.add_book(unused_book)

    library.borrow_book("M1", borrowed_book.isbn)

    result = library_module.rank_books_by_popularity(library)

    assert result == [borrowed_book, unused_book]