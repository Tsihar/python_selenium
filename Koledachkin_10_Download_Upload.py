import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# download_dir = os.path.join(os.getcwd(), "downloads")
# if not os.path.exists(download_dir):
#     os.makedirs(download_dir)

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": f"{os.getcwd()}\downloads" # спец параметр для установки места скачивания локально на компе
} # os.getcwd() - возвращает текущую директорию
options.add_experimental_option("prefs", prefs) # добавление prefs в опции
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options) # передача опций в драйвер

base_url_download = 'https://the-internet.herokuapp.com/download'
base_url_upload = 'https://the-internet.herokuapp.com/upload'
driver.get(base_url_download)
print(os.getcwd())
time.sleep(3)

# download
# driver.find_elements('xpath', '//a')[3].click()
#
# time.sleep(3)
#

# upload
driver.get(base_url_upload)
time.sleep(3)
upload_field = driver.find_element('xpath', '//input[@type="file"]')
upload_field.send_keys(f'{os.getcwd()}/downloads/upload.py')

time.sleep(3)

# base_url = ''
# driver.get(base_url)
#
#
# widget_frame = WebDriverWait(driver, 15).until(EC.visibility_of_element_located(("xpath", '//iframe[@name="sh-widget"]')),
#                                                       message=f"Can't find visible element by locator")(("xpath", '//iframe[@name="sh-widget"]'))
# time.sleep(6)
# widget_button = driver.find_element('xpath', '//button[contains(@class,"mantine-ActionIcon-root")]')
# widget_button.click()
# time.sleep(3)
#
# upload_field = driver.find_element('xpath', '//input[@type="file"]')
# upload_field.send_keys(f'{os.getcwd()}/downloads/Blackhole.png')
#
# time.sleep(5)