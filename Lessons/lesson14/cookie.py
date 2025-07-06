import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



chrome_options = Options()
chrome_options.add_argument('--window-size=1920,1080')
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://demoqa.com/login")

# print(driver.get_cookie("_ga"))

print(driver.get_cookies()) # получить все куки с сайта

driver.add_cookie({
    "name": "Example",
    "value": "ExampleValue",
})
time.sleep(2)
print(driver.get_cookie("Example")) # добавление своих куки

### ЗАМЕНА КУКИ ###

before = driver.get_cookie("SID")
print(before)

driver.delete_cookie("SID")
driver.add_cookie({
    "name": "SID",
    "value": "Pososi"
})

after = driver.get_cookie("SID")
print(after)

driver.delete_all_cookies()

driver.add_cookie({
    "name": "SID",
    "value": "Pososi"
})

after = driver.get_cookies()
print(after)