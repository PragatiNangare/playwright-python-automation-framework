from pages.DragPage import DragPage

def test_drag_drop(page):
    drag_drop_page = DragPage(page)
    drag_drop_page.load()
    initial_box_a = drag_drop_page.get_box_text("A")
    initial_box_b = drag_drop_page.get_box_text("B")
    drag_drop_page.drag_a_to_b()
    final_box_a = drag_drop_page.get_box_text("A")
    final_box_b = drag_drop_page.get_box_text("B")
    assert final_box_a == initial_box_b
    assert final_box_b ==initial_box_a


