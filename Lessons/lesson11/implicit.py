from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--window-size=1920,1080')

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.implicitly_wait(10)
driver.get('https://demoqa.com/dynamic-properties')
VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']") # - неявные ожидания
driver.find_element(*VISIBLE_AFTER_BUTTON).click()

