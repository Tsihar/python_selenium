import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
actions = ActionChains(driver)

# 1 простой дрэг н дроп
driver.get("https://the-internet.herokuapp.com/drag_and_drop")

A = ("xpath", "//div[@id='column-a']")
B = ("xpath", "//div[@id='column-b']")


locator_a = driver.find_element(*A)
locator_b = driver.find_element(*B)

actions.drag_and_drop(locator_a, locator_b).perform() # метод drag_and_drop, первый параметр что дрэгаем, второй - куда дропаем

time.sleep(2)

assert "//div[@id='column-b']//header[text()='B']" in driver.page_source, 'locator is not found' # проверка, что сделан дрэг н дроп


# 2 сложный дрэг н дроп

# driver.get("https://tympanus.net/Development/DragDropInteractions/sidebar.html")
# #
# drag = ("xpath", "(//div[@class='grid__item'])[2]")
# drop = ("xpath", "(//div[@class='drop-area__item'])[2]")
# #
# locator_drag = driver.find_element(*drag)
# locator_drop = driver.find_element(*drop)
#
# actions.click_and_hold(locator_drag) \
#     .pause(2) \
#     .move_to_element(locator_drop) \
#     .release() \
#     .perform()
#
# # кликнули и задержали, чтобы появился сайдбар > сайдбар появился, поуза 2 сек > переносим в место дропа > отпускаем лкп методом release > выполняем цепочку методом perform
#
# time.sleep(3)
