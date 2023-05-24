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

menu_checkbox = driver.find_element(by=By.XPATH, value="//li[@id='item-1']")
menu_checkbox.click()
print("menu_checkbox is checked")

#2 находим локатор чекбокса нужного (Home) и кликаем по нему
check_box = driver.find_element(by=By.XPATH, value="//span[@class='rct-title']")
check_box.click()
print("Home is checked")

#3 ОТКРОЕМ дерево чекбоксов под Homе
check_box = driver.find_element(by=By.XPATH, value="//button[@aria-label='Toggle']") # не отработало по вложенному локатору (кот в теге <svg>) в используемый, так что нужно еще внимательно выбирать локатор
check_box.click()
print("tree is opened")





