import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.page_load_strategy = "eager"
chrome_options.add_argument('--window-size=1920,1080')
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

#HECKBOX_1 = ("xpath", "//input[@type='checkbox'][1]")
#HECKBOX_2 = ("xpath", "//input[@type='checkbox'][2]")

#driver.get('https://the-internet.herokuapp.com/checkboxes')
#time.sleep(2)
#print(driver.find_element(*CHECKBOX_1).get_attribute('checked')) # None
#driver.find_element(*CHECKBOX_1).click()
#print(driver.find_element(*CHECKBOX_1).get_attribute('checked')) # true (type = str)
#print(driver.find_element(*CHECKBOX_1).is_selected()) # True

## CHECKBOX_HOME_STATUS = ("xpath", "//input[@id='tree-node-home']")
## CHECKBOX_HOME_ACTION = ("xpath", "//span[@class='rct-checkbox']")
##
## driver.get("https://demoqa.com/checkbox")
## print(driver.find_element(*CHECKBOX_HOME_STATUS).is_selected())
##
## driver.find_element(*CHECKBOX_HOME_ACTION).click()
## print(driver.find_element(*CHECKBOX_HOME_STATUS).is_selected())

driver.get("https://demoqa.com/selectable")

ELEMENT_ONE = ("xpath", "//li[text()='Cras justo odio']")

before = driver.find_element(*ELEMENT_ONE).get_attribute("class")
print(before)
driver.find_element(*ELEMENT_ONE).click()
after = driver.find_element(*ELEMENT_ONE).get_attribute("class")
assert "active" in after
time.sleep(3)





