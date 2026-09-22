class Book:
    def __init__(self, isbn, title, author, total_copies=1):
        if not isbn or not isbn.strip():
            raise ValueError("ISBN cannot be empty")

        if not title or not title.strip():
            raise ValueError("Book title cannot be empty")

        if total_copies < 0:
            raise ValueError("Total copies cannot be negative")

        self.isbn = isbn
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies
        self.rating = 0

    def add_rating(self, rating_value):
        if not isinstance(rating_value, (int, float)):
            raise ValueError("Rating must be a number between 0 and 5")

        if rating_value < 0 or rating_value > 5:
            raise ValueError("Rating must be between 0 and 5")

        self.rating = rating_value