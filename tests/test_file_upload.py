from pages.UploadPage import UploadPage
import pytest
import os


def test_file_upload(page):
    file_path = os.path.abspath("test_data/sample.txt")
    file_upload_page = UploadPage(page)

    file_upload_page.load()

    file_upload_page.upload_file(file_path).click_upload()

    result = file_upload_page.get_uploaded_filename()

    assert result == "sample.txt"
