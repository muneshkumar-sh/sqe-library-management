
import time

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.catalog_page import CatalogPage

pytestmark = pytest.mark.ui

def generate_isbn():
    base = "978" + str(time.time_ns())[-9:]

    total = sum(
        int(digit) * (1 if index % 2 == 0 else 3)
        for index, digit in enumerate(base)
    )

    check_digit = (10 - total % 10) % 10

    return base + str(check_digit)


@pytest.fixture
def catalog():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    try:
        page = CatalogPage(driver)
        page.open("http://127.0.0.1:5000/")
        yield page

    finally:
        driver.quit()


# TC-01: Add a book successfully.
def test_add_book(catalog):
    isbn = generate_isbn()

    catalog.add_book(
        "Software Engineering",
        isbn,
        "SQE Author",
        3
    )

    row = catalog.book_row_text(isbn)

    assert "Software Engineering" in row
    assert "SQE Author" in row
    assert isbn in row
    assert catalog.get_available_copies_display(isbn) == "3"


# TC-02: Borrow a book and verify available copies.
def test_borrow_book(catalog):
    isbn = generate_isbn()

    catalog.add_book(
        "Software Testing",
        isbn,
        "SQE Author",
        2
    )

    assert catalog.get_available_copies_display(isbn) == "2"

    catalog.borrow_book(isbn)

    assert catalog.wait_for_copies(isbn, 1) == "1"


# TC-03: Reject an empty title without calling the API.
def test_empty_title_validation(catalog):
    isbn = generate_isbn()

    catalog.monitor_add_book_requests()

    catalog.add_book(
        "",
        isbn,
        "SQE Author",
        2
    )

    message = catalog.wait_for_message("Title is required")

    assert "Title is required" in message
    assert catalog.add_book_request_count() == 0
    assert not catalog.book_exists(isbn)


# TC-04: Reject borrowing when no copies are available.
def test_borrow_unavailable_book(catalog):
    isbn = generate_isbn()

    catalog.add_book(
        "Last Copy Book",
        isbn,
        "SQE Author",
        1
    )

    assert catalog.get_available_copies_display(isbn) == "1"

    # Borrow the last available copy.
    catalog.borrow_book(isbn)

    assert catalog.wait_for_copies(isbn, 0) == "0"

    # Attempt to borrow again.
    catalog.borrow_book(isbn)

    message = catalog.wait_for_message("No copies available")

    assert "No copies available" in message
    assert catalog.get_available_copies_display(isbn) == "0"
