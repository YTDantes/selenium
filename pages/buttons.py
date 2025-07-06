class ButtonsCheck:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://demoqa.com/selectable")

    def select_grid(self):
        self.driver.find_element("xpath", "//a[@data-rb-event-key='grid']").click()

    def check_buttons(self, BUTTONS):
        buttons = self.driver.find_elements(*BUTTONS)
        for button in buttons:
            button.click()
            status = button.get_attribute("class")
            assert "active" in status
