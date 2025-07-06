import pytest

from pages.buttons import ButtonsCheck

BUTTONS = ("xpath", "//div/li[contains(@class, 'list-group-item')]")

# @pytest.mark.skip('Bug №42')
def test_button(driver):
    buttons = ButtonsCheck(driver)
    buttons.open()
    buttons.select_grid()
    buttons.check_buttons(BUTTONS)

# @pytest.mark.smoke  # pytest -v -s -m "not smoke"/smoke
# def test_1():
#     assert 1 == 1


