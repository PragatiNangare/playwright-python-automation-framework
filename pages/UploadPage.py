from config import BASE_URL
class UploadPage:
    def __init__ (self,page):
        self.page= page
        self.file_input = self.page.locator("#file-upload")
        self.upload_button = self.page.locator("#file-submit")
        self.uploaded_file = self.page.locator("#uploaded-files")

    def load(self):
        self.page.goto(f"{BASE_URL}/upload")

    def upload_file(self,path):
        self.file_input.set_input_files(path)
        return self
    
    def click_upload(self):
        self.upload_button.click()
        return self

    def get_uploaded_filename(self):
        return self.uploaded_file.text_content().strip()
    