class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def add_rating(self, rating):
        if rating < 0:
            raise ValueError("Rating cannot be negative")

        self.rating = rating