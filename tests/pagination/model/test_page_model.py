from src.pagination.model.page_model import Page


def test_page_model():
    assert Page(items=[], size=10, page=1, total=20, pages=2)
