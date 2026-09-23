from unittest.mock import patch

import pytest

from src.book import Book
from src.library import Library, LibraryIOError


@pytest.fixture
def export_library():
    library = Library()

    book1 = Book(
        "9780132350884",
        "Clean Code",
        "Robert C. Martin",
        total_copies=2,
    )

    book2 = Book(
        "9780135957059",
        "The Pragmatic Programmer",
        "Andrew Hunt",
        total_copies=1,
    )

    library.add_book(book1)
    library.add_book(book2)

    return library


def test_export_catalog_writes_expected_content(export_library):
    # Arrange
    expected_content_1 = (
        "9780132350884 | Clean Code | "
        "Robert C. Martin | Available: 2\n"
    )

    expected_content_2 = (
        "9780135957059 | The Pragmatic Programmer | "
        "Andrew Hunt | Available: 1\n"
    )

    # Act
    with patch("builtins.open") as mock_open:
        mock_file = mock_open.return_value.__enter__.return_value

        export_library.export_catalog("catalog.txt")

    # Assert
    assert mock_open.call_args.args[0] == "catalog.txt"
    assert mock_open.call_args.args[1] == "w"

    mock_file.write.assert_any_call(expected_content_1)
    mock_file.write.assert_any_call(expected_content_2)

    assert mock_file.write.call_count == 2


def test_export_catalog_raises_library_io_error(export_library):
    # Arrange
    with patch(
        "builtins.open",
        side_effect=OSError("Permission denied"),
    ):

        # Act & Assert
        with pytest.raises(
            LibraryIOError,
            match="Could not export catalog",
        ):
            export_library.export_catalog("catalog.txt")