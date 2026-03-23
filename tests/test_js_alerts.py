import pytest
from pages.AlertsPage import AlertsPage


def test_js_alert(page):
    alerts_page = AlertsPage(page)
    alerts_page.load()

    page.on("dialog", lambda dialog: dialog.accept())
    alerts_page.click_js_alert()
    result = alerts_page.get_result_text()
    assert result == "You successfully clicked an alert"

    page.on("dialog", lambda dialog: dialog.accept())
    alerts_page.click_js_confirm()
    clicked_ok = alerts_page.get_result_text()
    assert clicked_ok == "You clicked: Ok"


def test_js_cancel(page):
    alerts_page = AlertsPage(page)
    alerts_page.load()
    page.on("dialog", lambda dialog: dialog.dismiss())
    alerts_page.click_js_confirm()
    clicked_cancel=  alerts_page.get_result_text()
    assert clicked_cancel == "You clicked: Cancel"


def test_js_prompt_input(page):
    alerts_page = AlertsPage(page)
    alerts_page.load()
    page.on("dialog", lambda dialog: dialog.accept("pragati"))
    alerts_page.click_js_prompt()
    result = alerts_page.get_result_text()
    assert result == "You entered: pragati" 
    
    













 