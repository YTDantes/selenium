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

driver.get("https://demoqa.com/alerts")

BUTTON_1 = ("xpath", "//button[@id='alertButton']")
BUTTON_3 = ("xpath", "//button[@id='confirmButton']")
BUTTON_4 = ("xpath", "//button[@id='promtButton']")
# wait.until(EC.element_to_be_clickable(BUTTON_1)).click()
# wait.until(EC.element_to_be_clickable(BUTTON_3)).click()
wait.until(EC.element_to_be_clickable(BUTTON_4)).click() # ввод текста

# дожидаемся алерта

alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
time.sleep(3)
alert.send_keys("Danial") # ввести текст в алерт
alert.accept() # принять алерт
#print(alert.text) # посмотреть текст аллерта
# alert.accept()
#alert.dismiss()

time.sleep(5)
