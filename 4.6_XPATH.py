# Обращение к элементам по любому существующему локатору - XPATH
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

#1 # обращение к элементу по ID
# user_name = driver.find_element(by=By.ID, value="user-name")

#2 обращение к элементу по NAME
user_name = driver.find_element(by=By.NAME, value="user-name")

#3 обращение к элементу по Full XPATH (необходимо скопировать весь тег как XPATH в дев туле и вставить в "value=", только надо заменить на одинар ковычки)
# "*" значит будет поиск по всей html странице в не зав-ти от того, какой указан тег
# user_name = driver.find_element(by=By.XPATH, value="//*[@id='user-name']")
#
# 4 обращение к ID через XPATH (ID XPATH)
# - сначала идут 2 слэша //
# - затем ищем тег необх поля (в нашем случае <input>). Получаем "//input"
# - затем в квадратных скобках через собаку указываем к чему (какому локатору) мы обращаемся [@id='user-name']
# - в конеч итоге получаем //input[@id='user-name']
#
# user_name = driver.find_element(by=By.XPATH, value="//input[@id='user-name']")

#5 если у нас нет ни ID, ни NAME, но есть data-test. Соотв-но можно обратится к этому атрибуту
# user_name = driver.find_element(by=By.XPATH, value="//input[@data-test='username']")
user_name.send_keys("standard_user")