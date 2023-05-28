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

login_standard_user = "standard_user"
password_all = "secret_sauc"

user_name = driver.find_element(by=By.XPATH, value="//input[@id='user-name']")
user_name.send_keys(login_standard_user) # и тут
print("input login")
password = driver.find_element(by=By.XPATH, value="//input[@id='password']")
password.send_keys(password_all)
print("input password")
button_login = driver.find_element(by=By.XPATH, value="//input[@id='login-button']")
button_login.click()
print("click login button")

# проверка того, что система выдает ошибку на неверно введенный логин (для этого поменяем переменную с логином на какое-нить не верное значение, а пароль д б верным)
# warning_login = driver.find_element(by=By.XPATH, value="//*[@id='login_button_container']") # по xpath нашли локатор сообщения об ошибке
# warning_message_login = warning_login.text # сохраняем текст сообщения об ошибке
# print(warning_message)
#
# assert warning_message_login == "Epic sadface: Username and password do not match any user in this service"
# print("Correct") # убеждаемся что фактич текст ошибки равен тому, что мы ожидаем

# проверка того, что система выдает ошибку на неверно введенный пароль (для этого поменяем переменную с паролем на какую-нить не верное значение, а логин д б верным)
warning_password = driver.find_element(by=By.XPATH, value="//*[@id='login_button_container']") # тот же самый локатор для пароля т к сообщения об ошибке одни и те же
warning_message_password = warning_password.text # сохраняем текст сообщения об ошибке
print(warning_message_password)

assert warning_message_password == "Epic sadface: Username and password do not match any user in this service"
print("Correct")