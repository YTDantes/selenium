import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.vk.com/")
print("Текущий title:", driver.title)
driver.get("https://www.ya.ru/")
print("Текущий title:", driver.title)
driver.back()
assert driver.current_url == "https://vk.com/", "Не получилось вернуться"
driver.refresh()
url = driver.current_url
print("Текущий URL:", url)
driver.forward()
assert driver.current_url == "https://ya.ru/", "Не вернулись на яндекс"


time.sleep(3)