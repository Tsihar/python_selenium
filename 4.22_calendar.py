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
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()

new_date = driver.find_element(by=By.XPATH, value="//input[@id='datePickerMonthYearInput']")
# #1 надо очистить поле где введена дата, т к там введена уже информация, а потом надо будет ввести новую
# new_date.send_keys(Keys.BACKSPACE*10)
# # new_date.clear()
# # поместим новое значение в поле даты (скопируем существующее)
# new_date.send_keys("05/08/2023")
# new_date.send_keys(Keys.RETURN)

#2 кликнем по самому календарю найдя необходимый локатор даты
# чтобы открыть календарь надо кликнуть в поле ввода
new_date.click()
# date_9 = driver.find_element(by=By.XPATH, value="//div[@aria-label='Choose Tuesday, May 9th, 2023']")
# date_9.click()

#3 если хотим выбрать сегодняшнее число
# на локаторе сегоднящней даты в значении атрибута class есть today, в отличие от остальных локаторов дат
# т о мы можем найти значение нужное по частичному локатору с помощью CONTAINS
# с пом метода contains мы можем искать уникальные элементы, в случае когда не можем найти локатор и т д
# new_date.click()
# current_date = driver.find_element(by=By.XPATH, value="//div[contains(@class,'react-datepicker__day--today')]")
# current_date.click()

#4 еще варик обращения к тому или иному числу - выбрать опред дату

# date_9 = driver.find_element(by=By.XPATH, value="//div[@aria-label='Choose Tuesday, May 9th, 2023']")
# взять дату из кода ниже (использовали для уникального названия скриншота)
date_now = datetime.datetime.utcnow().strftime("%d")
print(date_now)
date_tomorrow = int(date_now) + 1 # перевод в целые числа текущ даты, и + 1 для получения цифры соответствующей завтрашнему числу
locator = "//div[@aria-label='Choose Thursday, May " + str(date_tomorrow) + "th, 2023']"  # разбиваем локатор на 3 части
print(locator)
date_9 = driver.find_element(by=By.XPATH, value=locator)
date_9.click()





