from src.library import Library
import src.library as library_module


def test_rank_empty_library_returns_empty_list():
    library = Library()

    result = library_module.rank_books_by_popularity(library)

    assert result == []