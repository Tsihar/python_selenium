import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys

service = Service(executable_path=ChromeDriverManager().install())  # для драйвер-менеджера
driver = webdriver.Chrome(service=service)  # для драйвер-менеджера

# options = webdriver.ChromeOptions() # для обычного драйвера
# driver = webdriver.Chrome(options=options) # для обычного драйвера

demoqa1 = 'https://demoqa.com/checkbox'
demoqa2 = 'https://demoqa.com/selectable'
demoqa3 = 'https://demoqa.com/radio-button'
heroku = 'https://the-internet.herokuapp.com/dropdown'
wait = WebDriverWait(driver, 10, poll_frequency=1)
actions = ActionChains(driver)
driver.maximize_window()
"""Дропдауны"""
# они обычно в теге select, а теги option это значения, которые выбираем из списка

DD = ("xpath", "//select[@id='dropdown']")

# driver.get(heroku)
# обращаемся к элементу через класс Select, а дальше уже через него взаимодействуем с опциями дропдауна
# GET_DD = Select(driver.find_element(*DD))  # можно и find element-ом сделать
# wait.until(EC.element_to_be_clickable(DD))
# с эл-тами можно взаим-вать через индекс, текст и через значение атрибута value
# GET_DD.select_by_visible_text("Option 1") # по тексту
# # time.sleep(2)
# GET_DD.select_by_value("2") # значение атрибута value
# # time.sleep(2)
# GET_DD.select_by_index(1) # по индексу. индекс 0 - это дефолт когда ничег не выбрано
# time.sleep(2)
#
# """Получить все доступные опции дропдауна"""
# all_options = GET_DD.options
# print(all_options) # записался список веб элементов опций
#
# # перебор всех опций по тексту
# for option in all_options:
#     # time.sleep(2)
#     GET_DD.select_by_visible_text(option.text) # получаем текст каждого веб-элемента/опции
#     print(option.text)
#
# for option in all_options: # проверим, что опция есть дропдауне
#     # time.sleep(2)
#     if "Option 1" in option.text:
#         print("Опция присутствует")
#
# # перебор всех опций по индексу
# for option in all_options:
#     # time.sleep(2)
#     GET_DD.select_by_index(all_options.index(option)) # получаем индекс элемента в списке по его значению
#     print(all_options.index(option))
#
# # перебор всех опций по value
# for option in all_options:
#     # time.sleep(2)
#     GET_DD.select_by_value(option.get_attribute("value")) # для каждого элемента получаем атhибут value
#     print(option.get_attribute("value"))

"""Работа с клавиатурой"""
# driver.get("https://the-internet.herokuapp.com/key_presses")
#
# FIELD = ("xpath", "//input[@id='target']")
# GET_FIELD = driver.find_element(*FIELD)
# GET_FIELD.send_keys(Keys.BACKSPACE) # сымпортить класс Keys
# time.sleep(3)
# GET_FIELD.send_keys("sdfsdfasdf")
# GET_FIELD.send_keys(Keys.CONTROL + "A") # сочетание клавиш выделит текст выше
# time.sleep(3)


"""Селект и мультиселект"""

SELECT = ("xpath", "//input[@id='react-select-3-input']")
driver.get('https://demoqa.com/select-menu')
# GET_SELECT = driver.find_element(*SELECT)
# # в 2 этапа через send keys: сначала выбрать нужную опцию, а затем нажать Enter
# # GET_SELECT.send_keys("Ms.")
# # GET_SELECT.send_keys(Keys.ENTER)
# # time.sleep(3)
#
# # 2й способ выбора нужной опции - это через фриз страницы на 5 сек js кодом
# PROF_OPTION = ("xpath", "(//div[text()='Prof.'])[2]")
# GET_SELECT.click() # открыли дропдаун
#
# GET_PROF_OPTION = driver.find_element(*PROF_OPTION) # нашли опцию
#
# GET_PROF_OPTION.click() # кликнули по найденной опции

"""Мультиселект"""
# тоде надо найти инпут
MULTISELECT = ("xpath", "//input[@id='react-select-4-input']")
GET_MULTISELECT = driver.find_element(*MULTISELECT)
GET_MULTISELECT.send_keys("GRE")
GET_MULTISELECT.send_keys(Keys.TAB) # TAB дозаполнит оставшееся слово и выберет его
GET_MULTISELECT.send_keys("BLUE")
GET_MULTISELECT.send_keys(Keys.ENTER)

time.sleep(3)
