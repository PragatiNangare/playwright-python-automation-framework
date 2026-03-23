
from config import BASE_URL


class InputsPage:
    def __init__(self,page):
        self.page = page 
        self.input_field = page.locator("input[type='number']")

    def load(self):
        self.page.goto(f"{BASE_URL}/inputs")
    
    def enter_value(self,value):
        self.input_field.type(str(value))

    def get_value(self):
        return self.input_field.input_value() 
    
    def increment_value(self):
        self.input_field.click()
        self.input_field.press("ArrowUp")

    def decrement_value(self):
        self.input_field.click()
        self.input_field.press("ArrowDown")

    def clear_input(self):
        self.input_field.fill("")

