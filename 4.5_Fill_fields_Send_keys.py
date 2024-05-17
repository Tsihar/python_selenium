import time

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Firefox(executable_path='/geckodriver.exe')
# driver.get('https://www.saucedemo.com/')
# driver.maximize_window()
# user_name = driver.find_element_by_id("user-name")
# система сначала зачеркивает find_element_by_id(), потому что этот способ устарел
# идем от простого к сложному, чтобы мы понимали по приходу на проект, что актуально, а что нет
# user_name = driver.find_element(By.ID, "user-name") # более новый метод
# система предлагает импортировать модуль для того, чтобы выбранный метод работал
# обращаемся к переменной driver и методу find_element указывая локатор вестки (айдишник)
# user_name.send_keys("standard_user")
# обращаясь к переменной user_name и методу send_keys, указываем логин

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
# driver.maximize_window()

user_name = driver.find_element(by=By.ID, value="user-name")
user_name.send_keys("standard_user")

user_name = driver.find_element(by=By.ID, value="password")
user_name.send_keys("secret_sauce")

enter = driver.find_element(by=By.ID, value="login-button")
enter.send_keys(Keys.RETURN)

current_url = driver.current_url # получить URL текущей страницы
print(current_url)

current_title = driver.title # возвращает title из раметки страницы, если он есть
print(current_title)

# click_enter = driver.find_element(by=By.XPATH, value="//button[@type='submit']")
# click_enter.click()

print(driver.page_source) # получения всего исходного кода страницы

time.sleep(10)
driver.close()

