import pytest 
from pages.WindowsPage import WindowsPage

def test_new_tab(page):
    windows_page = WindowsPage(page)
    windows_page.load()

    context = page.context

    with context.expect_page() as new_page_info:
        windows_page.click_click_here()

    new_page = new_page_info.value

    result = new_page.text_content("h3")

    assert result.strip() == "New Window"