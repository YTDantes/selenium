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

YES_RADIO_STATUS = ("xpath", "//input[@id='yesRadio']")
YES_RADIO = ("xpath", "//label[@for='yesRadio']")
NO_RADIO_STATUS = ("xpath", "//input[@id='noRadio']")
NO_RADIO = ("xpath", "//label[@for='noRadio']")

driver.get("https://demoqa.com/radio-button")
status = driver.find_element(*YES_RADIO_STATUS).is_selected()
print(status)
driver.find_element(*YES_RADIO).click()
status = driver.find_element(*YES_RADIO_STATUS).is_selected()
print(status)
print(driver.find_element(*NO_RADIO_STATUS).is_enabled())
time.sleep(2)