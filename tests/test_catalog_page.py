import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.catalog_page import CatalogPage
pytestmark = pytest.mark.ui

def test_add_book_through_catalog_page():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    try:
        catalog = CatalogPage(driver)

        catalog.open("http://127.0.0.1:5000/")

        isbn = "9780132350884"

        catalog.add_book(
            "Python Programming",
            isbn,
            "John Smith",
            3
        )

        # Verify that the book appears in the catalog
        row = catalog.book_row_text(isbn)

        assert "Python Programming" in row
        assert "John Smith" in row

        # Verify available copies
        copies = catalog.get_available_copies_display(isbn)

        assert copies == "3"

    finally:
        driver.quit()
