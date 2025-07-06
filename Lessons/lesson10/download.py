import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": f"{os.getcwd()}\\downloads", # создание папки для загрузок
}
chrome_options.add_experimental_option("prefs", prefs)

chrome_options.add_argument('--window-size=1920,1080') # разрешение

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/download")
time.sleep(3)
driver.find_elements("xpath", "//a")[5].click()
time.sleep(3)
