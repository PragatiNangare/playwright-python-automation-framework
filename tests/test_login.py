import pytest
import allure
from playwright.sync_api import expect
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage


@pytest.mark.parametrize("username,password,expected",[
        ("tomsmith","SuperSecretPassword!","success"),
       ( "wrong_username","pssword","fail")

    ])
@pytest.mark.smoke
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_login(page,username,password,expected):
    login_page = LoginPage(page)
    login_page.load()
    
    login_page.login(username,password)

    if expected== "success":
        expect(login_page.flash_message).to_contain_text("You logged into a secure area!")
    else:
        expect(login_page.flash_message).to_contain_text("invalid")

@pytest.mark.regression
def test_logout(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    login_page.load()
    login_page.login("tomsmith", "SuperSecretPassword!")
    home_page.logout()
    expect(home_page.flash_message).to_contain_text("You logged out")
