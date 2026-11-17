from flask import Flask, jsonify, request

from src.book import Book
from src.library import (
    Library,
    MAX_BORROW_LIMIT,
    validate_isbn,
    calculate_fine,
)

def create_app(library=None, member_ids=None):
    app = Flask(__name__)

    # Reuse the existing Library class.
    library = library or Library()

    # Member registration is configured at the API layer.
    members = set(member_ids if member_ids is not None else {501})

    # Store fines separately because the existing Library
    # class does not maintain fine records.
    member_fines = {member_id: 0 for member_id in members}

    app.extensions["libraryhub_library"] = library
    app.extensions["libraryhub_members"] = members
    app.extensions["libraryhub_fines"] = member_fines

    def error_response(message, status_code):
        return jsonify({"error": message}), status_code

    def book_response(book):
        return {
            "title": book.title,
            "isbn": book.isbn,
            "author": book.author,
            "available_copies": book.available_copies,
        }

    def get_json_body():
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return None

        return data

    # -------------------------------------------------
    # 1. POST /books - Add a book
    # -------------------------------------------------
    @app.route("/books", methods=["POST"])
    def add_book():
        data = get_json_body()

        if data is None:
            return error_response("Request body must be a JSON object", 400)

        required_fields = ["title", "isbn", "author"]

        for field in required_fields:
            if field not in data:
                return error_response(
                    f"Missing required field: {field}", 400
                )

        title = data["title"]
        isbn = data["isbn"]
        author = data["author"]
        total_copies = data.get("total_copies", 1)

        if not all(
            isinstance(value, str) and value.strip()
            for value in (title, isbn, author)
        ):
            return error_response(
                "Title, ISBN and author must be non-empty strings", 400
            )

        if isinstance(total_copies, bool) or not isinstance(total_copies, int):
            return error_response(
                "total_copies must be an integer", 400
            )

        if total_copies < 0:
            return error_response(
                "total_copies cannot be negative", 400
            )

        try:
            validate_isbn(isbn)
        except ValueError as error:
            return error_response(str(error), 400)

        if isbn in library.books:
            return error_response("Book already exists", 400)

        try:
            book = Book(
                isbn=isbn,
                title=title,
                author=author,
                total_copies=total_copies,
            )
            library.add_book(book)

        except (ValueError, TypeError) as error:
            return error_response(str(error), 400)

        return jsonify(book_response(book)), 201

    # -------------------------------------------------
    # 2. GET /books/<isbn> - Retrieve a book
    # -------------------------------------------------
    @app.route("/books/<isbn>", methods=["GET"])
    def get_book(isbn):
        book = library.books.get(isbn)

        if book is None:
            return error_response("Book not found", 404)

        return jsonify(book_response(book)), 200

    # -------------------------------------------------
    # 3. POST /members/<id>/borrow - Borrow a book
    # -------------------------------------------------
    @app.route("/members/<int:member_id>/borrow", methods=["POST"])
    def borrow_book(member_id):
        if member_id not in members:
            return error_response("Member not found", 404)

        data = get_json_body()

        if data is None:
            return error_response("Request body must be a JSON object", 400)

        isbn = data.get("isbn")

        if not isinstance(isbn, str) or not isbn.strip():
            return error_response(
                "A valid ISBN is required", 400
            )

        book = library.books.get(isbn)

        if book is None:
            return error_response("Book not found", 404)

        if book.available_copies <= 0:
            return error_response("No available copies", 400)

        current_loans = library.loans.get(member_id, [])

        if len(current_loans) >= MAX_BORROW_LIMIT:
            return error_response("Borrow limit exceeded", 400)

        try:
            library.borrow_book(member_id, isbn)
        except ValueError as error:
            return error_response(str(error), 400)

        book.available_copies -= 1

        return jsonify({
            "member_id": member_id,
            "isbn": isbn,
            "available_copies": book.available_copies,
        }), 200

    # -------------------------------------------------
    # 4. POST /members/<id>/return - Return a book
    # -------------------------------------------------
    @app.route("/members/<int:member_id>/return", methods=["POST"])
    def return_book(member_id):
        if member_id not in members:
            return error_response("Member not found", 404)

        data = get_json_body()

        if data is None:
            return error_response("Request body must be a JSON object", 400)

        isbn = data.get("isbn")

        if not isinstance(isbn, str) or not isbn.strip():
            return error_response(
                "A valid ISBN is required", 400
            )

        book = library.books.get(isbn)

        if book is None:
            return error_response("Book not found", 404)

        current_loans = library.loans.get(member_id, [])

        if isbn not in current_loans:
            return error_response(
                "This book is not borrowed by this member", 400
            )

        current_loans.remove(isbn)
        book.available_copies += 1

        return jsonify({
            "member_id": member_id,
            "isbn": isbn,
            "available_copies": book.available_copies,
            "message": "Book returned successfully",
        }), 200

    # -------------------------------------------------
    # 5. GET /members/<id>/fines - Retrieve fines
    # -------------------------------------------------
    @app.route("/members/<int:member_id>/fines", methods=["GET"])
    def get_member_fines(member_id):
        if member_id not in members:
            return error_response("Member not found", 404)

        fine = member_fines.get(member_id, 0)

        return jsonify({
            "member_id": member_id,
            "fine": fine,
        }), 200

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
