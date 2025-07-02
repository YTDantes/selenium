import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://hyperskill.org/login?next=/study-plan&utm_source=homepage")
time.sleep(3)
driver.find_elements("class name", "nav-link")[3].click()
elements = driver.find_elements("class name", "nav-link")
for element in elements:
    print(element.text)
time.sleep(5)