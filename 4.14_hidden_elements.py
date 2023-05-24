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
# driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(by=By.XPATH, value="//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("input login")
password = driver.find_element(by=By.XPATH, value="//input[@id='password']")
password.send_keys(password_all)
print("input password")
password.send_keys(Keys.RETURN)

#1 откроем бургер меню, чтобы увидеть элементы меню, которые скрыты и появляются только после открытия меню
menu = driver.find_element(by=By.XPATH, value="//button[@id='react-burger-menu-btn']")
menu.click()
print("menu is opened")
time.sleep(1)

#2 обратимся к пункту меню about
about_link = driver.find_element(by=By.XPATH, value="//a[@id='about_sidebar_link']")
about_link.click()
print("about page is opened")
time.sleep(1)

#3 (самопрактика) заферифаим, что мы зашли на нужную страницу (по урлу) и заделаем скриншот
url_about = 'https://saucelabs.com/'
get_url_about = driver.current_url
assert url_about == get_url_about
print("about is correct")
time.sleep(3)

current_date = datetime.datetime.utcnow().strftime("%d.%m.%Y.%H.%M.%S")
screenshot_name = f'screenshot_{current_date}.png'
driver.save_screenshot("C:\\Users\\Просто юзер\\PycharmProjects\\python_selenium\\Screenshots\\" + screenshot_name)



