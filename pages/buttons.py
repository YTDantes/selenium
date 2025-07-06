class ButtonsCheck:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://demoqa.com/selectable")


    def select_grid(self):
        self.driver.find_element("xpath", "//a[@data-rb-event-key='grid']").click()


    def check_buttons(self, BUTTONS):
        buttons = self.driver.find_elements(*BUTTONS)
        for i in range(2):
            count = 0
            for button in buttons:
                button.click()
                status = button.get_attribute("class")
                count += 1
                try:
                    assert "active" in status, print("Кнопка ", count, " не активна")
                    print("Кнопка ", count, " активна")
                except:
                    pass