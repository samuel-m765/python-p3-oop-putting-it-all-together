class Book:
    def __init__(self, title, author, pages, price):
        if not title:
            raise ValueError("Title cannot be empty")
        if not author:
            raise ValueError("Author cannot be empty")  # <-- new validation
        if pages <= 0:
            raise ValueError("Pages must be greater than zero")
        if price < 0:
            raise ValueError("Price cannot be negative")

        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
