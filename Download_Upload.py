import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys

# download_dir = os.path.join(os.getcwd(), "downloads")
# if not os.path.exists(download_dir):
#     os.makedirs(download_dir)

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": f"{os.getcwd()}\downloads"
} # os.getcwd() - возвращает текущую директорию
options.add_experimental_option("prefs", prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
base_url = 'https://the-internet.herokuapp.com/download'
driver.get(base_url)
print(os.getcwd())
time.sleep(3)

driver.find_elements('xpath', '//a')[3].click()

time.sleep(3)