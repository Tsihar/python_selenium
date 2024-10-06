from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait # явное ожидание
from selenium.webdriver.support import expected_conditions as EC # будем указывать условие для ожидания



service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
demoqa = 'https://demoqa.com/dynamic-properties'
heroku = 'https://the-internet.herokuapp.com/dynamic_controls'

# 1 не явные ожидания
# используется 1 раз для всего кода, сколько сек задали, столько и будет ожидание для всех элементов
# минус их в том, что если надо проверить исчезновение кнопки, то неявными проверить не сможем
# driver.implicitly_wait(10) # будет ждать 10 сек до появления эл-та

# driver.get(base_url)
# VISIBLE_AFTER_5_SECS = ("xpath", "//button[@id='visibleAfter']")
# get_visible_after_5_secs = driver.find_element(*VISIBLE_AFTER_5_SECS).click()

# глобально, надо использовать только 1 вид ожиданий, не смешивать их

# 2 лучше использовать явные ожидания
# в них мы ждем определенного условия (появление/исчезновение элемента, изменение текста или состояния эл-та и т д )
# явное ожидание мы указываем для КАЖДОГО элемента, в отличие от неявного (одно ожидание на все элементы)

# driver.get(demoqa)
# 2.1 ожидание элемента который появится

# VISIBLE_AFTER_5_SECS = ("xpath", "//button[@id='visibleAfter']")
wait = WebDriverWait(driver, 15, poll_frequency=1) # прокидываем драйвер, кол-во сек ожидания условия, как часто мы опрашиваем страницу (раз в 1 сек)
# GET_VISIBLE_AFTER_5_SECS = wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_5_SECS)) # ждем когда появится видимый элемент, можно не распаковывать, т к метод принимает кортеж и распаковывает
# # тут возвращается веб эл-нт, поэтому можно записать в переменную и кликать по нему
# GET_VISIBLE_AFTER_5_SECS.click()
#
# driver.refresh()

# 2.2 ожидание элемента, который раздисейблится
# ENABLED_IN_5_SECS = ("xpath", "//button[@id='enableAfter']")
# GET_AVAILABLE_BUTTON = wait.until(EC.element_to_be_clickable(ENABLED_IN_5_SECS))
# GET_AVAILABLE_BUTTON.click()

# 2.3 исчезновение кнопки после нажатия
driver.get(heroku)
REMOVE_BUTTON = ("xpath", "//button[text()='Remove']")
GET_REMOVE_BUTTON = driver.find_element(*REMOVE_BUTTON)
GET_REMOVE_BUTTON.click()

wait.until(EC.invisibility_of_element_located(REMOVE_BUTTON))
print("кнопка исчезла")

# 2.4 после нажатия кнопки дождаться что поле станет кликабельным
ENABLE_BUTTON = ("xpath", "//button[text()='Enable']")
INPUT_FIELD = ("xpath", "//input[@type='text']")
GET_ENABLE_BUTTON = wait.until(EC.element_to_be_clickable(ENABLE_BUTTON)) # для четкости кода все кнопки надо делать через явное ожидание
GET_ENABLE_BUTTON.click()

GET_INPUT_FIELD = wait.until(EC.element_to_be_clickable(INPUT_FIELD))
GET_INPUT_FIELD.send_keys("Hello")
wait.until(EC.text_to_be_present_in_element_value(INPUT_FIELD, "Hello")) # делаем проверку, что мы действительно ввели текст
print("текст введен в поле ввода")