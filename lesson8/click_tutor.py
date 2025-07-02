import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10) # Время поиска элемента
driver.maximize_window()

driver.get('https://hyperskill.org/login?next=/study-plan')
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

email_field = driver.find_element(By.XPATH, "//input[@placeholder='E-mail']")
assert email_field.get_attribute('value') == "", "поле не пустое"

email_field.send_keys('dan12332123@gmail.com')
value = email_field.get_attribute('value')
assert "dan12332123@gmail.ru" in value, "Неверный email"
email_field.clear()
time.sleep(3)