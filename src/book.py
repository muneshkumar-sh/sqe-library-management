class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author

    def add_rating(self, rating_value):
        if rating_value < 0 or rating_value > 5:
            raise ValueError("Rating must be between 0 and 5")

        self.rating = rating_value