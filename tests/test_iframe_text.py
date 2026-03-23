import pytest 
from pages.IframePage import IframePage


def test_iframe_text(page):
    iframe_page = IframePage(page)
    iframe_page.load()

    text = iframe_page.get_text()
    assert text == "Your content goes here."
