import os
import time
import pickle # новый импорт
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = Options()
chrome_options.add_argument('--disable-blink-features=AutomationControlled') # теперь браузер будет думать что мы человек
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36') # можно менять юзер агент сайты

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://stepik.org/lesson/1164785/step/1?unit=1177128")

driver.add_cookie({
    "name": "username",
    "value": "user123",
})


driver.refresh()
time.sleep(5)

cookie = driver.get_cookie("username")

assert cookie["value"] == "user123"
print(cookie)
time.sleep(5)

driver.delete_cookie("_ym_d")
driver.refresh()
time.sleep(5)




# cookies = pickle.load(open(os.getcwd()+"\cookies\cookies.pkl", "rb"))  # должна произойти авторизация на сайте со своими куками
# for cookie in cookies:
#     driver.add_cookie(cookie)
#
time.sleep(5)
driver.refresh()
time.sleep(5)