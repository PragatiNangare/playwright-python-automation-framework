
from config import BASE_URL
class AlertsPage():
    def __init__(self,page):
        self.page = page
        self.js_alert_btn= page.locator("text=Click for JS Alert")
        self.js_confirm_btn = page.locator("text=Click for JS Confirm")
        self.js_prompt_btn = page.locator("text=Click for JS Prompt")
        self.result_text = page.locator("#result")
        

    def load(self):
        self.page.goto(f"{BASE_URL}/javascript_alerts")

    def click_js_alert(self):
        self.js_alert_btn.click()

    def click_js_confirm(self):
        self.js_confirm_btn.click()

    def click_js_prompt(self):
        self.js_prompt_btn.click()

    def get_result_text(self):
        return self.result_text.text_content()
    

