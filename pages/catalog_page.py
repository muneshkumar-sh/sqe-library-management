from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CatalogPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def add_book(self, title, isbn, author, copies):
        fields = {
            "title-input": title,
            "isbn-input": isbn,
            "author-input": author,
            "copies-input": str(copies)
        }

        for field_id, value in fields.items():
            element = self.wait.until(
                EC.visibility_of_element_located(
                    (By.ID, field_id)
                )
            )
            element.clear()
            if value:
                element.send_keys(value)

        self.driver.find_element(By.ID, "add-btn").click()

    def book_row_text(self, isbn):
        row = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, f"row-{isbn}")
            )
        )
        return row.text

    def get_available_copies_display(self, isbn):
        element = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, f"available-copies-{isbn}")
            )
        )
        return element.text.strip()

    def borrow_book(self, isbn, member_id=501):
        member = self.driver.find_element(By.ID, "memberId")
        member.clear()
        member.send_keys(str(member_id))

        field = self.driver.find_element(By.ID, "borrowIsbn")
        field.clear()
        field.send_keys(isbn)

        self.wait.until(
            EC.element_to_be_clickable((By.ID, "borrow-btn"))
        ).click()

    def wait_for_copies(self, isbn, expected):
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.ID, f"available-copies-{isbn}"),
                str(expected)
            )
        )

        return self.get_available_copies_display(isbn)

    def wait_for_message(self, expected):
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.ID, "message"), expected
            )
        )

        return self.driver.find_element(By.ID, "message").text

    def monitor_add_book_requests(self):
        self.driver.execute_script("""
            window.addBookRequests = 0;
            const originalFetch = window.fetch;

            window.fetch = function(resource, options) {
                const url = new URL(
                    resource instanceof Request
                        ? resource.url : resource,
                    window.location.href
                );

                const method = (
                    options?.method ||
                    resource?.method ||
                    "GET"
                ).toUpperCase();

                if (url.pathname === "/books" && method === "POST") {
                    window.addBookRequests++;
                }

                return originalFetch.apply(this, arguments);
            };
        """)

    def add_book_request_count(self):
        return self.driver.execute_script(
            "return window.addBookRequests;"
        )

    def book_exists(self, isbn):
        return bool(
            self.driver.find_elements(By.ID, f"row-{isbn}")
        )
