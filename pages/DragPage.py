from config import BASE_URL

class DragPage():
    def __init__(self,page):
        self.page = page
        self.box_a = page.locator("#column-a")
        self.box_b = page.locator("#column-b")


    def load(self):
        self.page.goto(f"{BASE_URL}/drag_and_drop")

    def drag_a_to_b(self):
        # reliable approach for CI
        self.box_a.hover()
        self.page.mouse.down()
        self.page.wait_for_timeout(200)
        self.box_b.hover()
        self.page.mouse.up()
        return self
    
    def get_box_text(self,box):
        if box=="A":
            return  self.box_a.locator("header").text_content().strip()
        else:
            return  self.box_b.locator("header").text_content().strip()
        
