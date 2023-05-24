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
base_url = 'https://demoqa.com/'
driver.get(base_url)
driver.maximize_window()

#1 кликаем по Elements
# action = ActionChains(driver) # без перехода на элемент не хотело работать, потом заработало
elements = driver.find_element(by=By.XPATH, value="//*[@id='app']/div/div/div[2]/div/div[1]")
# action.move_to_element(elements).perform() # без перехода на элемент не хотело работать, потом заработало
# time.sleep(1) # без слипа не хотело работать, потом заработало (хз, че такое)
elements.click()
print("elements is clicked")

menu_radio_button = driver.find_element(by=By.XPATH, value="//li[@id='item-2']")
menu_radio_button.click()
print("menu_radio_button is checked")

#2 находим локатор радио батона и кликаем по нему
# impressive_radio = driver.find_element(by=By.XPATH, value="//input[@id='yesRadio']") # при выполнении по этому локатору будет ошибка в системе, и в ошибка система подсказывает какой элемент интерактивный
# impressive_radio = driver.find_element(by=By.XPATH, value="//label[@for='yesRadio']")
# impressive_radio.click()
# print("impressive_radio is checked")

# проверим, что выбрали действительно yes
# yes = driver.find_element(by=By.XPATH, value="//*[@id='app']/div/div/div[2]/div[2]/div[2]/p/span")
# yes_value = yes.text
# assert yes_value == "Yes"
# print("yes is chosen")

#3 по css селектору кликнем по yes
yes = driver.find_element(by=By.CSS_SELECTOR, value="label.custom-control-label[for='yesRadio']")
yes.click()
# label - тэг, custom-control-label - следующий атрибут class (точкой разделяются для указания пути), [for='yesRadio'] - сиснтаксис следующего интерактивного/кликабельного атрибута yesRadio


