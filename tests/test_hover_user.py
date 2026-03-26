from pages.HoverPage import HoverPage

def test_hover_user(page):
    hover_page = HoverPage(page)
    hover_page.load()
    hover_page.hover_on_user(0)
    result = hover_page.get_user_text(0)
    assert "user1" in result



