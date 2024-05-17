
# можно обращаться по id, name, class_name, xpath, link_text, tag_name

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

user_name = driver.find_element(by=By.XPATH, value="//input[@data-test='username']")
user_name.send_keys("standard_user")

#1 обратимся к полю по CSS селектору
password = driver.find_element(by=By.CSS_SELECTOR, value="#password") # value вставляется путем копирования selector (ПКМ > copy selector)
password.send_keys("secret_sauce")

#2 обратимся к кнопке login с кликом по кнопке login и как результат залогинимся на сайте
button_login = driver.find_element(by=By.XPATH, value="//input[@value='Login']") # обращаемся по xpath к любому локатору относящемуся к кнопке
button_login.click() # метод click позволяет делать клик по любому контролу

