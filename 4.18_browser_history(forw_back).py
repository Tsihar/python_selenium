import datetime
import time

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

menu = driver.find_element(by=By.XPATH, value="//button[@id='react-burger-menu-btn']")
menu.click()
print("menu is opened")
time.sleep(1)

about_link = driver.find_element(by=By.XPATH, value="//a[@id='about_sidebar_link']")
about_link.click()
print("about page is opened")
time.sleep(1)

# иногда сложно перемещаться по страницам, легче использ браузерные кнопки вперед и назад, на практике это применяется довольно часто
#1 вернемся назад по истории бразузера (нажмем кнопку back браузера)
driver.back()
print("go back")
time.sleep(2)

#2 вернемся вперед по истории бразузера (нажмем кнопку forward браузера)
driver.forward()
print("go forward")
time.sleep(2)



