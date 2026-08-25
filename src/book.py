class Book:
    def __init__(self, isbn, title, author):
        if not isbn or not isbn.strip():
            raise ValueError("ISBN cannot be empty")

        self.isbn = isbn
        self.title = title
        self.author = author

    def add_rating(self, rating_value):
        if not isinstance(rating_value, (int, float)):
            raise ValueError("Rating must be a number between 0 and 5")

        if rating_value < 0 or rating_value > 5:
            raise ValueError("Rating must be between 0 and 5")

        self.rating = rating_value

# book management practice

# improve book details

# prepare book functionality

# rebase practice complete