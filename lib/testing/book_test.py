import pytest
from lib.book import Book

def test_book_creation():
    b = Book("1984", "George Orwell", 328, 9.99)
    assert b.title == "1984"
    assert b.author == "George Orwell"
    assert b.pages == 328
    assert b.price == 9.99

def test_invalid_title():
    with pytest.raises(ValueError):
        Book("", "Author", 100, 10)

def test_invalid_author():
    with pytest.raises(ValueError):
        Book("Title", "", 100, 10)

def test_invalid_pages():
    with pytest.raises(ValueError):
        Book("Title", "Author", 0, 10)

    with pytest.raises(TypeError):
        Book("Title", "Author", "not an int", 10)

def test_invalid_price():
    with pytest.raises(ValueError):
        Book("Title", "Author", 100, -5)

    with pytest.raises(TypeError):
        Book("Title", "Author", 100, "not a number")
