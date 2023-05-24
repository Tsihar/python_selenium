# 1 скролл нужен для случая когда элемент не виден и надо проскроллить
# 2 также когда надо сделать скриншот и части экрана, кот не попадает на экран
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
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
# driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(by=By.XPATH, value="//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("input login")
password = driver.find_element(by=By.XPATH, value="//input[@id='password']")
password.send_keys(password_all)
print("input password")
password.send_keys(Keys.RETURN)

# 3 сделаем просто скролл
# driver.execute_script("window.scrollTo(X, Y)") # метод execute_script позволяет перемещаться по странице
# параметр X - по горизонтали в пикселях
# параметр Y - по вертикали в пикселях
# если вместо X и Y поставить (0, 0), то это значит верхний левый угол

# зададим параметры и запустим тест
# driver.execute_script("window.scrollTo(0, 200)") # происходит скролл страницы на 200 пикселей вниз по вертикали
# можно заккоментить сверху driver.maximize_window(), чтоб видно было скролл хорошо

# 4 сделаем скролл для скриншота
# time.sleep(2) # можно поставить слип на случай, если скрин делается раньше скролла
# current_date = datetime.datetime.utcnow().strftime("%d.%m.%Y.%H.%M.%S")
# screenshot_name = f'screenshot_{current_date}.png'
# driver.save_screenshot("C:\\Users\\Просто юзер\\PycharmProjects\\python_selenium\\Screenshots\\" + screenshot_name)

# 5 рассмотрим варик когда нам нужно наводиться на эл-нт, но мы не знаем сколько надо скроллить,
# чтоб увидеть нужный нам эл-нт и к тому же разрешения на сервере и на разных мошинах могут быть разные
# и в рез-те задавая скролл на разных машинах он отработает по-разному

action = ActionChains(driver) # переменная action показывает каким именно браузером мы хотим управлять
red_t_shirt_add_to_cart = driver.find_element(by=By.XPATH, value="//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
# переменная red_t_shirt_add_to_cart, где мы храним локатор необходимого элемента, кот ниже по странице
ActionChains.move_to_element(red_t_shirt_add_to_cart).perform()
# скроллим страницу к нашему элементу с пом метода move_to_element
time.sleep(2) # можно поставить слип на случай, если скрин делается раньше скролла
current_date = datetime.datetime.utcnow().strftime("%d.%m.%Y.%H.%M.%S")
screenshot_name = f'screenshot_{current_date}.png'
driver.save_screenshot("C:\\Users\\Просто юзер\\PycharmProjects\\python_selenium\\Screenshots\\" + screenshot_name)

