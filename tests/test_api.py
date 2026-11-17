import pytest

from src.api.app import create_app
from src.book import Book
from src.library import Library


@pytest.fixture
def library():
    """Create a fresh library with one book for each test."""
    test_library = Library()

    test_library.add_book(
        Book(
            "9780132350884",
            "Clean Code",
            "Robert C. Martin",
            total_copies=2,
        )
    )

    return test_library


@pytest.fixture
def app(library):
    """Create a Flask application with an isolated library."""
    return create_app(library=library, member_ids={501})


@pytest.fixture
def client(app):
    """Provide Flask's test client."""
    return app.test_client()


def test_add_book_positive(client):
    response = client.post(
        "/books",
        json={
            "title": "Python Basics",
            "isbn": "9780135957059",
            "author": "John Smith",
            "total_copies": 3,
        },
    )

    data = response.get_json()

    # Layer 1: Status code
    assert response.status_code == 201

    # Layer 2: Response schema
    assert set(data.keys()) == {
        "title", "isbn", "author", "available_copies"
    }
    assert all(isinstance(data[key], str) for key in
               ("title", "isbn", "author"))
    assert isinstance(data["available_copies"], int)

    # Layer 3: Response content
    assert data == {
        "title": "Python Basics",
        "isbn": "9780135957059",
        "author": "John Smith",
        "available_copies": 3,
    }


def test_get_book_positive(client):
    response = client.get("/books/9780132350884")
    data = response.get_json()

    assert response.status_code == 200

    assert set(data.keys()) == {
        "title", "isbn", "author", "available_copies"
    }
    assert isinstance(data["available_copies"], int)

    assert data == {
        "title": "Clean Code",
        "isbn": "9780132350884",
        "author": "Robert C. Martin",
        "available_copies": 2,
    }


def test_borrow_book_positive(client):
    response = client.post(
        "/members/501/borrow",
        json={"isbn": "9780132350884"},
    )

    data = response.get_json()

    assert response.status_code == 200

    assert set(data.keys()) == {
        "member_id", "isbn", "available_copies"
    }
    assert isinstance(data["member_id"], int)
    assert isinstance(data["isbn"], str)
    assert isinstance(data["available_copies"], int)

    assert data == {
        "member_id": 501,
        "isbn": "9780132350884",
        "available_copies": 1,
    }


def test_return_book_positive(client):
    # First borrow the book so that it can be returned.
    borrow_response = client.post(
        "/members/501/borrow",
        json={"isbn": "9780132350884"},
    )
    assert borrow_response.status_code == 200

    response = client.post(
        "/members/501/return",
        json={"isbn": "9780132350884"},
    )

    data = response.get_json()

    assert response.status_code == 200

    assert set(data.keys()) == {
        "member_id", "isbn", "available_copies", "message"
    }
    assert isinstance(data["member_id"], int)
    assert isinstance(data["available_copies"], int)
    assert isinstance(data["message"], str)

    assert data == {
        "member_id": 501,
        "isbn": "9780132350884",
        "available_copies": 2,
        "message": "Book returned successfully",
    }


def test_get_member_fines_positive(client):
    response = client.get("/members/501/fines")
    data = response.get_json()

    assert response.status_code == 200

    assert set(data.keys()) == {"member_id", "fine"}
    assert isinstance(data["member_id"], int)
    assert isinstance(data["fine"], (int, float))

    assert data == {
        "member_id": 501,
        "fine": 0,
    }



def test_get_nonexistent_book_returns_404(client):
    response = client.get("/books/9999999999999")
    data = response.get_json()

    assert response.status_code == 404
    assert set(data.keys()) == {"error"}
    assert data["error"] == "Book not found"


def test_borrow_book_with_zero_available_copies_returns_400(client, library):
    book = library.books["9780132350884"]
    book.available_copies = 0

    response = client.post(
        "/members/501/borrow",
        json={"isbn": "9780132350884"},
    )
    data = response.get_json()

    assert response.status_code == 400
    assert set(data.keys()) == {"error"}
    assert data["error"] == "No available copies"


def test_add_book_missing_title_returns_400(client):
    response = client.post(
        "/books",
        json={
            "isbn": "9780135957059",
            "author": "John Smith",
            "total_copies": 3,
        },
    )
    data = response.get_json()

    assert response.status_code == 400
    assert set(data.keys()) == {"error"}
    assert data["error"] == "Missing required field: title"


def test_sixth_borrow_exceeds_limit(client, library):
    # Provide enough copies so the borrow limit is the only restriction.
    library.add_book(
        Book(
            "9780132350884",
            "Clean Code",
            "Robert C. Martin",
            total_copies=10,
        )
    )

    # Borrow five times successfully.
    for _ in range(5):
        response = client.post(
            "/members/501/borrow",
            json={"isbn": "9780132350884"},
        )
        assert response.status_code == 200

    # The sixth borrow must be rejected.
    response = client.post(
        "/members/501/borrow",
        json={"isbn": "9780132350884"},
    )
    data = response.get_json()

    assert response.status_code == 400
    assert set(data.keys()) == {"error"}
    assert data["error"] == "Borrow limit exceeded"



def test_get_all_books_full_schema(client):
    response = client.get("/books")
    data = response.get_json()

    # Layer 1: HTTP status
    assert response.status_code == 200

    # Layer 2: Full response schema
    assert isinstance(data, list)

    expected_keys = {
        "title",
        "isbn",
        "author",
        "available_copies",
    }

    for book in data:
        assert isinstance(book, dict)
        assert set(book.keys()) == expected_keys

        assert isinstance(book["title"], str)
        assert isinstance(book["isbn"], str)
        assert isinstance(book["author"], str)
        assert isinstance(book["available_copies"], int)

    # Layer 3: Actual response content
    assert data == [
        {
            "title": "Clean Code",
            "isbn": "9780132350884",
            "author": "Robert C. Martin",
            "available_copies": 2,
        }
    ]
