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
driver.delete_all_cookies()
cookies = pickle.load(open(os.getcwd()+"\cookies\cookies.pkl", "rb"))  # должна произойти авторизация на сайте со своими куками
for cookie in cookies:
    driver.add_cookie(cookie)

time.sleep(5)
driver.refresh()
time.sleep(5)