from config import BASE_URL
class CheckboxPage():
    def __init__(self,page):
        self.page = page
        self.checkboxes = page.locator("input[type='checkbox']")

    def load(self):
        self.page.goto(f"{BASE_URL}/checkboxes")


    def check_checkbox(self,index):
        self.checkboxes.nth(index).check()

    def uncheck_checkbox(self, index):
        self.checkboxes.nth(index).uncheck()

    def is_checked(self, index):
        return self.checkboxes.nth(index).is_checked()
    
    