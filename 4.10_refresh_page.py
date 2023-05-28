# это необходимо делать к прим для очистки полей либо для обновления инфы, которая подтянется только с рефрешем страницы
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

login_standard_user = "standard_use"
password_all = "secret_sauce"

user_name = driver.find_element(by=By.XPATH, value="//input[@id='user-name']")
user_name.send_keys(login_standard_user) # и тут
print("input login")
password = driver.find_element(by=By.XPATH, value="//input[@id='password']")
password.send_keys(password_all)
print("input password")
button_login = driver.find_element(by=By.XPATH, value="//input[@id='login-button']")
button_login.click()
print("click login button")

warning_login = driver.find_element(by=By.XPATH, value="//*[@id='login_button_container']")
warning_message_login = warning_login.text

assert warning_message_login == "Epic sadface: Username and password do not match any user in this service"
print("Correct")

# рефрещнем страницу для очистки полей логина и пароля
driver.refresh()