import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

demoqa = 'https://demoqa.com/dynamic-properties'
heroku = 'https://the-internet.herokuapp.com/checkboxes'
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get(heroku)

'''Чекбоксы'''
CHECKBOX_1 = ("xpath", "(//input[@type='checkbox'])[1]")
# GET_CHECKBOX_1 = wait.until(EC.element_to_be_clickable(CHECKBOX_1)) # прописывал через wait, не писал уже find_element
GET_CHECKBOX_1 = driver.find_element(*CHECKBOX_1)
GET_CHECKBOX_1.click() # в данной ситуации просто клик

'''Важно понимать в каком состоянии находится чекбокс'''
# Получение атрибута checked через get_attribute
print(GET_CHECKBOX_1.get_attribute("checked")) # на выходе true, но не булево тру, а стринговое, поэтому при проверках быть внимательным
GET_CHECKBOX_1.click()
print(GET_CHECKBOX_1.get_attribute("checked")) # на выходе None, т к мы анчекнули и его нету

# метод is_selected()
print(GET_CHECKBOX_1.is_selected()) # на выходе False булевый
GET_CHECKBOX_1.click()
print(GET_CHECKBOX_1.is_selected()) # на выходе True булево
time.sleep(3)