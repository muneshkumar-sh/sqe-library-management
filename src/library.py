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

        if len(current_books) >= MAX_BORROW_LIMIT: # <--- Used the constant here
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

def borrow_percentile(member, library):
    x = [len(v) for v in library.loans.values()]
    y = len(library.loans.get(member, []))
    n = len(x)
    r = sum(1 for a in x if a <= y)
    return (r / n) * 100

def parse_book_id(book_id_str):
    try:
        return int(book_id_str)
    except ValueError:  # <--- FIXED
        return -1


def calculate_fine(days_late):
    if days_late > FINE_GRACE_PERIOD: 
        return days_late * FINE_RATE_PER_DAY 
    return 0

def get_error():
    return BOOK_NOT_FOUND

def get_another_error():
    return BOOK_NOT_FOUND