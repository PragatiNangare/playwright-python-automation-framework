import pytest
from playwright.sync_api import sync_playwright
from config import BROWSER, HEADLESS


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = getattr(p,BROWSER).launch(headless = HEADLESS)
        context = browser.new_context()
        page = browser.new_page()
        yield page
        context.close()
        browser.close()
