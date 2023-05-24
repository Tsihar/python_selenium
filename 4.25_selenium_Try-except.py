import datetime
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
driver.maximize_window()

# 1 ищем кнопку, кот пока не появилась, но появится через 5 сек (намеренно вызываем ошибку системы)
# visible_button = driver.find_element(by=By.XPATH, value="//button[@id='visibleAfter']")
# visible_button.click()
# print("visible button is clicked")

# чтоб не получать ошибку можно поставить перед переменной sleep, но слипы это плохо, т к время прохождения тестов увеличивается
# но try/except помогает отлавливать такие моменты, и по-своему, в зав-ти от пробленого участка, их обрабатывать (перезагрузить, немного подождать и т д)

# например, есть момент при выполнении теста, когда какой-то косяк не всегда воспроизводимый, и его обоити помога ет рефреш страницы,
# и нам, чтоб тест был более стабильный, надо его делать, когда мы натыкаемся на эту ошибку.
# Мы в этот участок кода пишем try-except и при возникновенни косяка снова, он будет ловится и страница будет рефрешиться.

# 2 отловили название ошибки - NoSuchElementException - и делаем конструккцию try/except
# try:
#     visible_button = driver.find_element(by=By.XPATH, value="//button[@id='visibleAfter']")
#     visible_button.click()
# except NoSuchElementException as exception: #сначала имя ошибки пподчеркивается красным, т к оно не импортировано - импортируем
#     print("NoSuchElementException has been received") # выводим print? чтоб видеть, что поймали исключение
#     time.sleep(6) #указываем что хотим сделать в случае ошибки
#     visible_button = driver.find_element(by=By.XPATH, value="//button[@id='visibleAfter']") # делаем повторный клик на локатор, так как через 5 сек только появляется кнопка
#     visible_button.click()
#     print("visible button is clicked")

# 3 еще один сценарий с исключением (на странице радио батонов)
radio_button = driver.find_element(by=By.XPATH, value="//*[@id='item-2']")
radio_button.click()
try:

 # будем выбирать элемент yes
    yes_radio_button = driver.find_element(by=By.XPATH, value="//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[2]/label")
    yes_radio_button.click()
 # представим, что нам надо было получуть не Yes, а No (там выводится текст когда Yes выбираешь)
    message = driver.find_element(by=By.XPATH, value="//span[@class='text-success']")
    value_message = message.text # убедимся, что по локатору найден нужный нам текст
    print(value_message)

    assert value_message == "No" # делаем проверку на то, что мы ожидаем увидеть No

except AssertionError as exception: # нам надо рефрешнуть страницу, повторно кликнуть Yes и заверифаить в assert что нам нужно не No получить в сообщении, а Yes
    driver.refresh()
    time.sleep(3) # шоб увидть лучше
    yes_radio_button = driver.find_element(by=By.XPATH, value="//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[2]/label")
    yes_radio_button.click()
    message = driver.find_element(by=By.XPATH, value="//span[@class='text-success']")
    value_message = message.text
    print(value_message)

    assert value_message == "Yes"
    print("получено Yes в сообщении")

print('test is over')
# на выходе ловим ошибку AssertionError
# скажем системе, что нам надо делать с этой ошибкой с пом try/except
# после клика по Yes надо начинать Try, n к после него появляется сообщение содержащее Yes - 44 строка, и все эл-ты ниже tab-ом сдвигаем под try










