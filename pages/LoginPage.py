from config import BASE_URL

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator ("#username")
        self.password_input = page.locator ("#password")
        self.login_button = page.locator("button[type='submit']")
        self.flash_message = page.locator("#flash")

    def load(self):
        self.page.goto(f"{BASE_URL}/login")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        
    def logout(self):
        self.page.locator("a[href='/logout']").click()