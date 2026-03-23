import pytest
from pages.DropdownPage import DropdownPage


def test_default_dropdown_value(page):
    dropdown_page = DropdownPage(page)
    dropdown_page.load()
    actual = dropdown_page.get_selected_option()

    assert actual == ""


def test_select_option_1(page):
    dropdown_page = DropdownPage(page)
    dropdown_page.load()
    selected_option = "Option 1"
    dropdown_page.select_option(selected_option)
    actual = dropdown_page.get_selected_option()
    assert actual == "1"


def test_select_option_2(page):
    dropdown_page = DropdownPage(page)
    dropdown_page.load()
    selected_option = "Option 2"
    dropdown_page.select_option(selected_option)
    actual = dropdown_page.get_selected_option()
    assert actual == "2"


def test_dropdown_selection_replacement(page):
    dropdown_page = DropdownPage(page)
    dropdown_page.load()
    selected_option1 = "Option 1"
    selected_option2 = "Option 2"
    dropdown_page.select_option(selected_option1)
    dropdown_page.select_option(selected_option2)
    actual = dropdown_page.get_selected_option()
    assert actual == "2"

