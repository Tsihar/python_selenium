import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install()) # для драйвер-менеджера
driver = webdriver.Chrome(service=service) # для драйвер-менеджера

# options = webdriver.ChromeOptions() # для обычного драйвера
# driver = webdriver.Chrome(options=options) # для обычного драйвера

demoqa1 = 'https://demoqa.com/checkbox'
demoqa2 = 'https://demoqa.com/selectable'
demoqa3 = 'https://demoqa.com/radio-button'
heroku = 'https://the-internet.herokuapp.com/checkboxes'
wait = WebDriverWait(driver, 15, poll_frequency=1)

# driver.get(heroku)
#
# '''Чекбоксы'''
# CHECKBOX_1 = ("xpath", "(//input[@type='checkbox'])[1]")
# # GET_CHECKBOX_1 = wait.until(EC.element_to_be_clickable(CHECKBOX_1)) # прописывал через wait, не писал уже find_element
# GET_CHECKBOX_1 = driver.find_element(*CHECKBOX_1)
# GET_CHECKBOX_1.click() # в данной ситуации просто клик
#
# '''Важно понимать в каком состоянии находится чекбокс'''
# # Получение атрибута checked через get_attribute
# print(GET_CHECKBOX_1.get_attribute("checked")) # на выходе true, но не булево тру, а стринговое, поэтому при проверках быть внимательным
# GET_CHECKBOX_1.click()
# print(GET_CHECKBOX_1.get_attribute("checked")) # на выходе None, т к мы анчекнули и его нету
#
# # метод is_selected()
# print(GET_CHECKBOX_1.is_selected()) # на выходе False булевый
# GET_CHECKBOX_1.click()
# print(GET_CHECKBOX_1.is_selected()) # на выходе True булево
# time.sleep(3)

# """Нюанс 1, когда элемент перекрыт"""
# # когда элемент невидим мы сначала должны найти элемент для получения статуса, а затем для действия/клика и кликнуть по нему
# driver.get(demoqa1)
#
# ACTION_CHBOX = ("xpath", "//span[@class='rct-checkbox']")
# STATUS_CHBOX = ("xpath", "//input[@id='tree-node-home']") # чекбоксы реализуются инпутами
#
# print(driver.find_element(*STATUS_CHBOX).is_selected()) # до клика статус False
# GET_STATUS_CHBOX = driver.find_element(*ACTION_CHBOX)
# GET_STATUS_CHBOX.click()
# print(driver.find_element(*STATUS_CHBOX).is_selected()) # после клика статус True
# # просто на элементе не видно атрибута checked, но по проверке статуса видно, что он есть когда мы получаем True
# # т о мы можем проверить чекнутость чекбокса
#
# time.sleep(3)

# """Нюанс 2, когда чекбокс реализован не инпутом"""
#
# driver.get(demoqa2)
#
# CHKBOX = ("xpath", "//li[text()='Cras justo odio']")
# GET_CHKBOX = driver.find_element(*CHKBOX)
#
# before = GET_CHKBOX.get_attribute("class") # получим состояние атрибута класс до клика
# print(before) # mt-2 list-group-item list-group-item-action
# GET_CHKBOX.click()
# after = GET_CHKBOX.get_attribute("class") # получим состояние атрибута класс после клика
# print(after) # mt-2 list-group-item active list-group-item-action , добавляется значение active, по которому можно провалидировать состояние чекбокса
#
# assert "active" in after, "чет херня какая-то" # проверяем, что есть значение active в артибуте
#
# time.sleep(3)

"""Радиобатоны"""
# у них атрибут type="radio", у чекбоксов type="checkbox"
# чтоб проверить статус надо действовать как с чекбоксами, найти тег, по которому можно получить статус
driver.get(demoqa3)

RADIO_YES_STATUS = ("xpath", "//input[@id='yesRadio']")
GET_RADIO_YES_STATUS = driver.find_element(*RADIO_YES_STATUS)

RADIO_YES_ACTION = ("xpath", "//label[@class='custom-control-label']")
GET_RADIO_YES_ACTION = driver.find_element(*RADIO_YES_ACTION)

print(GET_RADIO_YES_STATUS.is_selected())
GET_RADIO_YES_ACTION.click()
print(GET_RADIO_YES_STATUS.is_selected()) # на локаторе ACTION до и после получили статус False, значит у него нет статуса

"""Радио батон задисейблен"""
RADIO_NO_STATUS = ("xpath", "//input[@id='noRadio']")
GET_RADIO_NO_STATUS = driver.find_element(*RADIO_NO_STATUS)
print(GET_RADIO_NO_STATUS.is_enabled(), "Проверен") # на выходе False, т к батон задисейблен. Так можно проверять любой другой элемент (кнопка, поле и тд)


time.sleep(3)
