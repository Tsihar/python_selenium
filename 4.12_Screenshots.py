import time
import datetime

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(by=By.XPATH, value="//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("input login")
password = driver.find_element(by=By.XPATH, value="//input[@id='password']")
password.send_keys(password_all)
print("input password")
password.send_keys(Keys.RETURN)

filter1 = driver.find_element(by=By.XPATH, value="//select[@class='product_sort_container']")
filter1.click()
filter1.send_keys(Keys.ARROW_DOWN)
time.sleep(2)
filter1.send_keys(Keys.RETURN)

# 1 делаем скриншот
# driver.save_screenshot('screenshot.png') # сохраняет в директорию проекта
# он делается очень быстро и мб не видна вся страница, поэтому можно перед выполнением команды поставить задержку
# если выполнить еще раз код, то файл замениться

# 2 делаем уникальное название файла при помощи добавления к нему даты
current_date = datetime.datetime.utcnow().strftime("%d.%m.%Y.%H.%M.%S")
# сымпортили модуль datetime (выдает текущую дату)
screenshot_name = f'screenshot_{current_date}.png'
driver.save_screenshot("C:\\Users\\Просто юзер\\PycharmProjects\\python_selenium\\Screenshots\\" + screenshot_name)
# пееред выполнением программы создали папку в проекте где хранится скринщоты будут
# указали путь где сохранять скринщот (созданная папка) и добавили имя скринщота сохраненное в переменную screenshot_name


