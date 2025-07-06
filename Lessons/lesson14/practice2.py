import os
import time
import pickle # новый импорт
from statistics import variance

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



chrome_options = Options()
chrome_options.add_argument('--disable-blink-features=AutomationControlled') # теперь браузер будет думать что мы человек
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36') # можно менять юзер агент сайты
chrome_options.add_argument('--window-size=1920,1080')
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://www.wildberries.ru/")
time.sleep(6)
CLOTHES_BUTTON = ("xpath", "//a//span[contains(text(), 'Завтра')]")
RAZMER_BUTTON = ("xpath", "//span[@class='sizes-list__size-ru']")
add_buttons = wait.until(EC.presence_of_all_elements_located(CLOTHES_BUTTON))
print(add_buttons)
print(len(add_buttons))
time.sleep(5)
for i in range(6):
    try:
        add_buttons[i].click()
        try:
            variante_button = wait.until(EC.element_to_be_clickable(RAZMER_BUTTON))
            variante_button.click()

        except:
            pass


    except Exception as e:
        print(e)

pickle.dump(driver.get_cookies(), open(os.getcwd()+"\cookies\practice.pkl", "wb"))

time.sleep(5)

driver.delete_all_cookies()
driver.refresh()


cookies = pickle.load(open(os.getcwd()+"\cookies\practice.pkl", "rb"))  # должна произойти авторизация на сайте со своими куками
for cookie in cookies:
    driver.add_cookie(cookie)

time.sleep(5)
driver.refresh()
time.sleep(5)




