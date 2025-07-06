import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://hyperskill.org/login?next=/study-plan&utm_source=homepage')
driver.find_element("xpath", '//button[@class = "btn btn-primary btn-sm !whitespace-nowrap" and @data-component-name = "Primitive"]').click()
time.sleep(5)