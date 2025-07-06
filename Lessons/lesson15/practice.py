import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.page_load_strategy = "eager"
chrome_options.add_argument('--window-size=1920,1080')
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

BUTTONS = ("xpath", "//div/li[contains(@class, 'list-group-item')]")

driver.get("https://demoqa.com/selectable")
driver.find_element("xpath", "//a[@data-rb-event-key='grid']").click()


buttons = driver.find_elements(*BUTTONS)
for button in buttons:
    button.click()
    status = button.get_attribute("class")
    assert "active" in status

for button in buttons:
    button.click()
    status = button.get_attribute("class")
    assert "active" in status
time.sleep(4)
