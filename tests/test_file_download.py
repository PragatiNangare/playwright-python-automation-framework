from pages.FileDownloadPage import FileDownloadPage
import pytest
import os


def test_file_download(page):
    file_name = "test-upload.txt"
    save_path = f"downloads/{file_name}"
    file_download_page = FileDownloadPage(page)
    file_download_page.load()
    download = file_download_page. download_file(file_name)

    download.save_as(save_path)
    assert os.path.exists(save_path)
    with open(save_path, "r") as file:
        content = file.read()

    assert "CREDO" in content   



