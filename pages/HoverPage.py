from config import BASE_URL
class HoverPage():
    def __init__(self,page):
        self.page = page
        self.users = page.locator(".figure")
    
    def load(self):
        self.page.goto(f"{BASE_URL}/hovers")
    
    def hover_on_user(self,index):
        self.users.nth(index).hover()
        return self
    
    def get_user_text(self,index):
        return self.users.nth(index).locator(".figcaption").text_content().strip()