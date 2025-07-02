import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--window-size=1920,1080') # разрешение

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/upload")

upload_field = driver.find_element("xpath", "//input[@type='file']")
upload_field.send_keys(f"{os.getcwd()}\\downloads\dummy.txt")
time.sleep(3)

# "//input[@type='file']" - эта конструкция чаще всего используется даже если загрузка через button а не через input