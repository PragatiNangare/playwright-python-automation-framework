from config import BASE_URL

class WindowsPage:
    def __init__(self, page):
        self.page = page
        self.click_here_link = page.locator("text=Click Here")

    def load(self):
        self.page.goto(f"{BASE_URL}/windows")

    def click_click_here(self):
        self.click_here_link.click()