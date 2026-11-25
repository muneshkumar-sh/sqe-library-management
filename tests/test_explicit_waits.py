
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from pages.catalog_page import CatalogPage


def generate_isbn():
    base = str(int(time.time() * 1000))[-12:].zfill(12)

    total = sum(
        int(digit) * (1 if index % 2 == 0 else 3)
        for index, digit in enumerate(base)
    )

    check_digit = (10 - total % 10) % 10
    return base + str(check_digit)


def test_borrow_book_with_explicit_wait():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    try:
        catalog = CatalogPage(driver)
        catalog.open("http://127.0.0.1:5000/")

        isbn = generate_isbn()

        catalog.add_book(
            "Explicit Wait Test Book",
            isbn,
            "SQE Lab",
            2
        )

        driver.find_element(By.ID, "borrowIsbn").send_keys(isbn)
        driver.find_element(By.ID, "borrow-btn").click()

        # Wait until the API request completes and copies update.
        WebDriverWait(driver, 5).until(
            lambda d: catalog.get_available_copies_display(isbn) == "1"
        )

        assert catalog.get_available_copies_display(isbn) == "1"

    finally:
        driver.quit()
