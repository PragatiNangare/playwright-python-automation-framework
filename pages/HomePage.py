class HomePage:
    def __init__(self,page):
        self.page = page
        self.logout_button = page.locator("a[href='/logout']")
        self.flash_message = page.locator("#flash")

    def logout(self):
        self.logout_button.click()