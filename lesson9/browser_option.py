import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "normal" # "eager" - без ожидания прогрузки всех элементов
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--incognito')
chrome_options.add_argument('--window-size=1920,1080') # разрешение
# chrome_options.add_argument('--ignore-certificate-errors') # ошибки связанные с сертификатами
# chrome_options.add_argument('--disable-cache') # отключение кэша
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

start_time = time.time()

driver.get('https://hyperskill.org/courses')
# driver.set_window_size(700, 700) то же самое разрешение
end_time = time.time()
result = end_time - start_time
print(result)