import datetime
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
# driver.maximize_window() #закомментим чтоб видеть консоль
# driver.implicitly_wait(10) # УКАЗЫВАЕМ ВРЕМЯ КОТОРОЕ СИСТЕМА БУДЕТ ЖДАТЬ ПОЯВЛЕНИЯ ЭЛЕМЕНТА В ДОМЕ
# ДАЛЬШЕ ЭТА КОМАНДА БУДЕТ ПРИМЕНИМА КО ВСЕМ ДЕЙСТВИЯМ КОТ МЫ БУДЕМ ИСПОЛЬЗОВАТЬ

# есть 2 вида ожидания - явное и неявное

# 1 неявное - когда ждем, что элемент появится в доме (разметке html) через опред промежуток времени,
# и начинаем с ним что-то делать(кликать, перетаскивать и тд)
# получим ошибку, т к мы не прописали ожидание появления кнопки visible after 5 secs
# print("start test")
# visible_button = driver.find_element(by=By.XPATH, value="//button[@id='visibleAfter']")
# visible_button.click()
# print("finish test")

# пропишем неявное ожидание
# print("start test")
# time.sleep(10)
# visible_button = driver.find_element(by=By.XPATH, value="//button[@id='visibleAfter']")
# visible_button.click()
# print("finish test")

# 1.2 неявное
# 10 сек поставили чтоб перестраховаться, на случай, если 5 не отрабатывает
# так делать нельзя, потому что тест по времени длится долго будет, а время надо сокращать
# поэтому надо прописывать неявное ожидание -- оно прописано в 19 строке !!!

# print("start test")
# visible_button = driver.find_element(by=By.XPATH, value="//button[@id='visibleAfter']")
# visible_button.click()
# print("finish test")

# 1.3 к примеру если написать неверно локатор, то неявное ожидание будет ждать 10 сек и тогда отвалится,
# несмотря на то, что кнопка, которую ждем, уже появилась через 5 сек

# print("start test")
# visible_button = driver.find_element(by=By.XPATH, value="//button[@id='visible']") # убралл в конце id After
# visible_button.click()
# print("finish test")

# почему сразу не поставить 60 сек, чтоб наверняка и не парится, что в теч какого времени какой-либо элемент не появится
# а потому что, каждая такая пауза это затягивание времени и по факту мы ждем элемента в нашем доме, а не на экране

# 2 явное ожидание - это когда мы под каждый элемент проставляем конкретное время ожидание, если это необходимо
# элемент доступен для клика - clickable
# элемент не только есть в доме (разметке), но и на странице виден - visible
# также элемент может быть на странице, но перекрыт баннером например, и тогда find_element его не найдет так как не увидит на странице

# нельзя вместе использовать явное и неявное ождания, инчае могут конфликтовать между собой

print("start test")
visible_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='visibleAfter']")))
# создали переменную, в кот сохранили класс WebDriverWait, в кот передаем наш драйвер и время,
# в теч которого мы будем взаимодействовать с нашим элементом. Каждые 0,5 сек частота вз-вия с эл-том
# EC (импорт прописан руками в 3ей строке) - expected condition, указывается то действие, кот ожидается для выполнения с элементом (на элемент можно бут нажать)
# will enable 5 seconds доступна для клика только через 5 сек
visible_button.click()
print("finish test")

# при implicit wait мы можем только работать с find element? а когда например надо определить, что элемент пропадает через какое-то время
# то в явном ожидании мы уже можем это прописывать, т к там есть такое ожидаемое условие
# также WebDriverWait позволяет уникально подходить к каждому элементу и с ним работать

