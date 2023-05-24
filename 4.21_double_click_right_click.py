import datetime
import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/buttons'
driver.get(base_url)
driver.maximize_window()

#1 двойной клик
action = ActionChains(driver) # переменная action явл экз-ром класса actionChains, в кот мы передаём наш драйвер
double_button = driver.find_element(by=By.XPATH, value="//button[@id='doubleClickBtn']")
action.double_click(double_button).perform() # обращаемся к экз класса action выполняя методы double_click, с указанием объекта клика, и perform()
# метод perform нужен для сохранения результата двойного клика (слова Смита), но судя по функции этого класса, метод запилен для выполнения всех методов прописанных в обращении к экземпляру класса action

# проверим по классике, что действительно кликнулось через assertion
note_click = driver.find_element(by=By.XPATH, value="//*[@id='doubleClickMessage']")
note_click_value = note_click.text
note = "You have done a double click"
assert note_click_value == note
print("double click has actually been made")

#1 правый клик - context_click
right_click_button = driver.find_element(by=By.XPATH, value="//button[@id='rightClickBtn']")
action.context_click(right_click_button).perform()
print("right click has actually been made")









