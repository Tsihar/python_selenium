from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/' # удобно передавать url через переменную, так как можно создать несколько урлов и далее передавать их в метод get, особенно в ООП
driver.get(base_url)
driver.maximize_window()

# user_name = driver.find_element(by=By.XPATH, value="//input[@id='user-name']") # обратимся по xpath к локатору id для поля login
# user_name.send_keys("standard_user")
#
# password = driver.find_element(by=By.XPATH, value="//input[@id='password']") # обратимся по xpath к локатору id для поля password
# password.send_keys("secret_sauce")
#
# button_login = driver.find_element(by=By.XPATH, value="//input[@id='login-button']") # обратимся по xpath к локатору id для кнопки Login
# button_login.click()

# 1 Для логина и пароль можно тоже передавать в переменных
login_standard_user = "standard_user" # тут, обозвали так потому что есть 4ре разных юзера под которыми можно логиниться, и всех надо в разные переменные пихать
password_all = "secret_sauce"

user_name = driver.find_element(by=By.XPATH, value="//input[@id='user-name']")
user_name.send_keys(login_standard_user) # и тут
print("input login") #будем выводить на печать что мы сделали
password = driver.find_element(by=By.XPATH, value="//input[@id='password']")
password.send_keys(password_all)
print("input password") #будем выводить на печать что мы сделали
button_login = driver.find_element(by=By.XPATH, value="//input[@id='login-button']")
button_login.click()
print("click login button") #будем выводить на печать что мы сделали

# 2 Убедимся, что это необх нам страница, необходимо обратится к какому -либо элементу на данной странице, считать какой-л текст (распарсить)
# название PRODUCTS есть только на той странице, котор открылась после логина, соотв удобно брать его

# обратимся по xpath к class-у
# text_products = driver.find_element(by=By.XPATH, value="//span[@class='title']")
# value_text_products = text_products.text #через метод text считали текст, и запомнили в переменной value_text_products
# print(value_text_products) # проверим, что мы считали корректное значение. В ответе Products значит все корректно отработало.
# Эта проверка показывает, что регистрация прошла успешно

# 3 проверим, что нашем искомое слово действительно Produсts и в этом поможет условные оператор Assert
# assert value_text_products == "Products"
# Этот оператор означает, что мы будем производить сравнение переменной value_text_products (читает локатор со значением Products) и зн-ние которое мы задали
# print("GOOD") # и если они равны, то слово GOOD выведется на печать, а иначе будет ошибка

# 4 есть еще url нашей заглавной страницы, он меняется реже, чем текст на странице, поэтому лучше чекать по нему, что мы залогинились и находимся на правильной странице
url = "https://www.saucedemo.com/inventory.html"
get_url = driver.current_url # обращаясь к переменной driver и методу current_url, мы сохраняем в переменной get_url текущее/фактическое значение урла
print(get_url)
assert get_url == url
print("Good URL")
# можно убрать в логине последнюю букву или по-другому изменить логин или пароль, и запустить код,
# тогда наш assert тоже упадет, но со стороны переменной get url, так как она не будет равна переменной url
# из-за зафейленого логина и НЕ перехода на страницу Products
