
MAX_BORROW_LIMIT = 5
FINE_GRACE_PERIOD = 14
FINE_RATE_PER_DAY = 5
BOOK_NOT_FOUND = "Book not found"


def fine_tier(days_overdue):
    if days_overdue < 0:
        raise ValueError("Days overdue cannot be negative")
    elif days_overdue == 0:
        return "None"
    elif days_overdue <= 7:
        return "Low"
    elif days_overdue <= 14:
        return "Medium"
    elif days_overdue <= 30:
        return "High"
    else:
        return "Severe"


class LibraryIOError(Exception):
    """Raised when the library catalog cannot be exported."""
    pass


class Library:
    def __init__(self):
        self.loans = {}
        self.books = {}

    def add_book(self, book):
        self.books[book.isbn] = book

    def total_available_copies(self):
        return sum(
            book.available_copies
            for book in self.books.values()
        )

    def export_catalog(self, path):
        try:
            with open(path, "w", encoding="utf-8") as file:
                for book in self.books.values():
                    content = (
                        f"{book.isbn} | {book.title} | "
                        f"{book.author} | Available: {book.available_copies}\n"
                    )
                    file.write(content)
        except OSError as error:
            raise LibraryIOError(
                f"Could not export catalog: {error}"
            ) from error

    def borrow_book(self, member_id, isbn):
        current_books = self.loans.get(member_id, [])

        if len(current_books) >= MAX_BORROW_LIMIT:
            raise ValueError("Borrow limit exceeded")

        current_books.append(isbn)
        self.loans[member_id] = current_books


def validate_isbn(isbn):
    if not isbn:
        raise ValueError("ISBN cannot be empty")

    if len(isbn) != 13:
        raise ValueError("ISBN must contain exactly 13 digits")

    if not isbn.isdigit():
        raise ValueError("ISBN must contain only numeric digits")

    return True


def rank_books_by_popularity(library):
    borrow_counts = {}

    for borrowed_books in library.loans.values():
        for isbn in borrowed_books:
            borrow_counts[isbn] = borrow_counts.get(isbn, 0) + 1

    return sorted(
        library.books.values(),
        key=lambda book: (
            -borrow_counts.get(book.isbn, 0),
            book.title.lower()
        )
    )


def borrow_percentile(member, library):
    if not library.loans:
        raise ValueError("Cannot calculate percentile for empty library")

    if member not in library.loans:
        raise ValueError("Member not found")

    borrow_counts = [
        len(books) for books in library.loans.values()
    ]

    member_count = len(library.loans[member])

    lower_count = sum(
        1 for count in borrow_counts
        if count < member_count
    )

    return (lower_count / len(borrow_counts)) * 100


def parse_book_id(book_id_str):
    try:
        return int(book_id_str)
    except ValueError:
        return -1


def calculate_fine(days_late):
    if days_late > FINE_GRACE_PERIOD:
        return days_late * FINE_RATE_PER_DAY
    return 0


def get_error():
    return BOOK_NOT_FOUND


def get_another_error():
    return BOOK_NOT_FOUND
