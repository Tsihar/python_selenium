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
base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'
driver.get(base_url)
driver.maximize_window()

action = ActionChains(driver)
time.sleep(2)
# image = driver.find_element(by=By.XPATH, value="//input[@id='id3']")
# action.click_and_hold(image).move_by_offset(200, 0).release().perform()
# print('200 +')
# click_and_hold - кликаем и тянем, в скобках указываем переменную, которую тянем и через
# точку указываем новый метод move_by_offset со значениями x и y, x - горизонтальная тяяга
# y - вертикальная тяга
# по вертикали не тянем поэтому 0, по горизонтали интересующее нас значение
# далее указываем через точку метод release? означающий, что мы отпускаем мышку
# в конце указываем perform(), чтобы сохранить/выполнить наше действие
# если указываем положительное число то тянется вправо, если отицательное - влево

#2 круглый ползунок (скролл пониже)
driver.execute_script("window.scrollTo(0, 3000)")

circle_slider = driver.find_element(by=By.XPATH, value="//*[@id='myRange']")
# time.sleep(2)
# action.move_to_element(circle_slider).perform()
# time.sleep(2)
action.click_and_hold(circle_slider).move_by_offset(-200, 0).release().perform()
print('200 -')

msfgoC2QQmbfmGT



