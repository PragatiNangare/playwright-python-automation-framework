import pytest
from pages.InputsPage import InputsPage


def test_enter_valid_number(page):
    inputs_page = InputsPage(page)
    inputs_page.load()
    value= "10"
    inputs_page.enter_value(value)
    actual = inputs_page.get_value()
    assert actual == value


def test_enter_invalid_input(page):
    inputs_page = InputsPage(page)
    inputs_page.load()
    value="abc"
    inputs_page.enter_value(value)
    actual= inputs_page.get_value()
    assert actual == ""

def test_increment_decrement(page):
    inputs_page = InputsPage(page)
    inputs_page.load()
    value="10"
    inputs_page.enter_value(value)
    inputs_page.increment_value()
    incremented_value = inputs_page.get_value()
    assert incremented_value == str(int(value) +1 )
    inputs_page.decrement_value()
    decremented_value = inputs_page.get_value()
    assert decremented_value == str(int(incremented_value) -1 )

def test_clear_input(page):
    inputs_page = InputsPage(page)
    inputs_page.load()
    value="10"
    inputs_page.enter_value(value)
    inputs_page.clear_input()
    actual = inputs_page.get_value()
    assert actual == ""
    





