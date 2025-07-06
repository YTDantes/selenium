from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 30, poll_frequency=1)

driver.get("https://omayo.blogspot.com/")

UNVISIBLE_TEXT = ("xpath", "//div[@id='deletesuccess']")
VISIBLE_TEXT = ("xpath", "//div[@id='delayedText']")
ENABLE_BUTTON = ("xpath", "//input[@id='timerButton']")
DISABLE_BUTTON = ("xpath", "//button[@id='myBtn']")

wait.until(EC.invisibility_of_element_located(UNVISIBLE_TEXT), message="Текст не исчез")
wait.until(EC.visibility_of_element_located(VISIBLE_TEXT), message="Текст не стал видимым")
wait.until(EC.element_to_be_clickable(ENABLE_BUTTON), message="Кнопка не стала активной")
driver.find_element("xpath", "//button[text()='Try it']").click()
wait.until_not(EC.element_to_be_clickable(DISABLE_BUTTON), message="Кнопка не деактивировалась")
print("Все тесты пройдены")