import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10) # Время поиска элемента
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/status_codes")
elements = driver.find_elements("xpath", "//li/a")
for element in elements:
    element.click()
    time.sleep(2)
    driver.back()
