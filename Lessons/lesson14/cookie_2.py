import os
import time
import pickle # новый импорт
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://demoqa.com/login")

LOGIN_FIELD = ("xpath", "//input[@placeholder='UserName']")
PASSWORD_FIELD = ("xpath", "//input[@placeholder='Password']")
BUTTON_LOGIN = ("xpath", "//button[@id='login']")

driver.find_element(*LOGIN_FIELD).clear()
driver.find_element(*LOGIN_FIELD).send_keys("dan12332123@gmail.com")
driver.find_element(*PASSWORD_FIELD).clear()
driver.find_element(*PASSWORD_FIELD).send_keys("Suhovd@niil2001")
driver.find_element(*BUTTON_LOGIN).click()

pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies.pkl", "wb")) # сохранение всех кукие в файл
# альше можно удалить авторизацию
