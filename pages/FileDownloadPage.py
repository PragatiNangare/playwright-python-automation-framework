from config import BASE_URL

class FileDownloadPage():
    
    def __init__(self,page):
        self.page = page
        
    def load(self):
        self.page.goto(f"{BASE_URL}/download")

    def download_file(self,file_name):
        with self.page.expect_download() as download_info:
            self.page.locator(f"text={file_name}").click()

        download = download_info.value
        return download
