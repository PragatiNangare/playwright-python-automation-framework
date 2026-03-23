from config import BASE_URL


class DropdownPage():
    def __init__(self,page):
        self.page = page
        self.dropdown_menu = page.locator("#dropdown")

    def load(self):
        self.page.goto(f"{BASE_URL}/dropdown")

    def select_option(self,option):
        self.dropdown_menu.select_option(label=option)

    def get_selected_option(self):
        return self.dropdown_menu.input_value()

