import pytest 
from pages.CheckboxPage import CheckboxPage


def test_checkbox_default_state(page):
    checkboxes_page = CheckboxPage(page)
    checkboxes_page.load()
    checkbox1_state = checkboxes_page.is_checked(0)
    assert checkbox1_state== False
    checkbox2_state= checkboxes_page.is_checked(1)
    assert checkbox2_state== True
    

def test_check_checkbox(page):
    checkboxes_page = CheckboxPage(page)
    checkboxes_page.load()
    checkboxes_page.check_checkbox(0)
    checkbox1_checked =checkboxes_page.is_checked(0)
    assert checkbox1_checked


def test_uncheck_checkbox(page):
    checkboxes_page = CheckboxPage(page)
    checkboxes_page.load()
    checkboxes_page.uncheck_checkbox(1)
    checkbox2_checked= checkboxes_page.is_checked(1)
    assert not checkbox2_checked

def test_checkbox_toggle(page):
    checkboxes_page = CheckboxPage(page)
    checkboxes_page.load()
    initial_state = checkboxes_page.is_checked(0)
    checkboxes_page.check_checkbox(0)
    new_state = checkboxes_page.is_checked(0)
    assert initial_state!= new_state
    
    






    








