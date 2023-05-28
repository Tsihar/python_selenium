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

# 1 удаление нжатием на backspace и возрат букв обратно
# user_name = driver.find_element(by=By.XPATH, value="//input[@id='user-name']")
# user_name.send_keys(login_standard_user)
# print("input login")
# time.sleep(3) # поставили слип чтоб увидеть удаление нагляднее
# user_name.send_keys(Keys.BACKSPACE) # (из вебрайвера импортировали либу Keys) BACKSPACE позволяет нажимать эту кнопку на клаве
# time.sleep(3)
# user_name.send_keys(Keys.BACKSPACE) # дублируем строку, если надо удалить еще 1 символ, и так далее в зав-ти сколько нам надо удалить букв
# time.sleep(3)
# user_name.send_keys("er") # добавим две выше удаленные буквы

# а вообще удобно просто умножить backspace на нужное кол-во символоав, кот надо удалить
# user_name.send_keys(Keys.BACKSPACE * 10)

# можно вообще полностью чистить заполненное поле
# user_name.clear()

# 2 Команда Enter
# user_name = driver.find_element(by=By.XPATH, value="//input[@id='user-name']")
# user_name.send_keys(login_standard_user)
# print("input login")
# password = driver.find_element(by=By.XPATH, value="//input[@id='password']")
# password.send_keys(password_all)
# print("input password")
# password.send_keys(Keys.RETURN) # Нажатие Enter. Даже удобнее, чем использовать ф-ю click с обращением к элементу по xpath
# button_login = driver.find_element(by=By.XPATH, value="//input[@id='login-button']")
# button_login.click()
# print("click login button")

# 3 клавиши вверх и вниз для перемещения выделенной опции по дропдауну
user_name = driver.find_element(by=By.XPATH, value="//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("input login")
password = driver.find_element(by=By.XPATH, value="//input[@id='password']")
password.send_keys(password_all)
print("input password")
password.send_keys(Keys.RETURN)

filter1 = driver.find_element(by=By.XPATH, value="//select[@class='product_sort_container']")
filter1.click()
filter1.send_keys(Keys.ARROW_DOWN) # нажатие кнопки стрелка вниз
time.sleep(2)
filter1.send_keys(Keys.RETURN) # нажатие Enter по выбранной опции дропдауна (сортируем Z-A)
# бывает неудобно на практике кликать на опцию дропдауна(локатор плохой или еще что-то) удобнее просто нажать стрелку для выбора опции