import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from pages.catalog_page import CatalogPage


def generate_isbn():
    base = str(int(time.time() * 1000))[-12:].zfill(12)

    total = sum(
        int(digit) * (1 if index % 2 == 0 else 3)
        for index, digit in enumerate(base)
    )

    check_digit = (10 - total % 10) % 10
    return base + str(check_digit)


def test_borrow_book_with_fixed_sleep():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    try:
        catalog = CatalogPage(driver)
        catalog.open("http://127.0.0.1:5000/")

        isbn = generate_isbn()

        catalog.add_book(
            "Fixed Sleep Test Book",
            isbn,
            "SQE Lab",
            2
        )

        # Confirm the book has been added.
        assert catalog.get_available_copies_display(isbn) == "2"

        # Borrow the book.
        driver.find_element(By.ID, "borrowIsbn").send_keys(isbn)
        driver.find_element(By.ID, "borrow-btn").click()

        # Deliberately insufficient fixed wait.
        time.sleep(0.2)

        copies = driver.find_element(
            By.ID, f"available-copies-{isbn}"
        ).text.strip()

        assert copies == "1"

    finally:
        driver.quit()
