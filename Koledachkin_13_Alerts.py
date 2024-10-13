import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
from selenium.webdriver.support.ui import WebDriverWait  # явное ожидание
from selenium.webdriver.support import expected_conditions as EC  # будем указывать условие для ожидания
svc = webdriver.ChromeService(executable_path=binary_path)
driver = webdriver.Chrome(service=svc)
demoqa = 'https://demoqa.com/alerts'
heroku = 'https://the-internet.herokuapp.com/dynamic_controls'
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get(demoqa)

# 1 Алерт с одной кнопкой
# ALERT_1 = ('xpath', '//button[@id="alertButton"]')
# GET_IMMEDIATE_ALERT = wait.until(EC.element_to_be_clickable(ALERT_1))
# time.sleep(3)
# GET_IMMEDIATE_ALERT.click()
#
# alert_1 = wait.until(EC.alert_is_present()) # после появления алерта мы его считываем и кладем в переменную
#
# driver.switch_to.alert # переключение на алерт, не надо указывать alert_1
# time.sleep(3)
# alert_1.accept() # нажатие OK в алерте
# time.sleep(3)

# 2 Алерт с 2мя кнопка и отклонить его
# ALERT_WITH_CANCEL = ('xpath', '//button[@id="confirmButton"]')
# GET_ALERT_WITH_CANCEL = wait.until(EC.element_to_be_clickable(ALERT_WITH_CANCEL))
# time.sleep(3)
# GET_ALERT_WITH_CANCEL.click()
#
# alert_with_cancel = wait.until(EC.alert_is_present()) # после появления алерта мы его считываем и кладем в переменную
#
# driver.switch_to.alert # переключение на алерт, не надо указывать alert_1
# time.sleep(3)
# print(alert_with_cancel.text) # получение текста алерта
# alert_with_cancel.dismiss() # нажатие Cancel в алерте
# time.sleep(3)

# 3 Ввод текста в алерт
ALERT_WITH_INPUT = ('xpath', '//button[@id="promtButton"]')
GET_ALERT_WITH_INPUT = wait.until(EC.element_to_be_clickable(ALERT_WITH_INPUT))
time.sleep(3)
GET_ALERT_WITH_INPUT.click()

alert_with_cancel = wait.until(EC.alert_is_present()) # после появления алерта мы его считываем и кладем в переменную

driver.switch_to.alert # переключение на алерт, не надо указывать alert_1
time.sleep(3)
alert_with_cancel.send_keys('Ihar') # ввод текста в алерт
time.sleep(3)
alert_with_cancel.accept()
time.sleep(3)