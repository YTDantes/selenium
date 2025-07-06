from pages.buttons import ButtonsCheck

BUTTONS = ("xpath", "//div/li[contains(@class, 'list-group-item')]")

def test_button(driver):
    buttons = ButtonsCheck(driver)
    buttons.open()
    buttons.select_grid()
    buttons.check_buttons(BUTTONS)
