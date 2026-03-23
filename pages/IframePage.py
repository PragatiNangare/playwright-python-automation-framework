from config import BASE_URL

class IframePage():
    def __init__(self, page):
        self.page = page
        self.iframe = page.frame_locator("#mce_0_ifr")
        self.text_area = self.iframe.locator("#tinymce")

    def load(self):
        self.page.goto(f"{BASE_URL}/iframe")

    def get_text(self):
        return self.text_area.text_content()
    