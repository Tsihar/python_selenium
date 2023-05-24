import datetime
import time

from selenium import webdriver
from selenium.webdriver import Keys
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

"""INFO product #1"""
product_1 = driver.find_element(by=By.XPATH, value="//a[@id='item_4_title_link']")
value_product_1 = product_1.text #сохраняем в переменную название продукта
print(value_product_1)

price_product_1 = driver.find_element(by=By.XPATH, value="//div[@class='inventory_item_price']")
value_price_product_1 = price_product_1.text #сохраняем в переменную название продукта
print(value_price_product_1)

"""Add product_sl_backpack to cart"""
select_product_1 = driver.find_element(by=By.XPATH, value="//button[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print("select product 1")

"""Transfer to the cart"""
cart = driver.find_element(by=By.XPATH, value="//a[@class='shopping_cart_link']")
cart.click()
print("Transfer to the cart")

"""INFO cart product #1""" #копипаст кода выше, но с добавлением cart в названиях переменной и изменением локаторов (локаторы не поменялись, но бывает что меняются)
cart_product_1 = driver.find_element(by=By.XPATH, value="//a[@id='item_4_title_link']")
cart_value_product_1 = cart_product_1.text #сохраняем в переменную название продукта
print(cart_value_product_1)
assert cart_value_product_1 == value_product_1 # нужны asserts для проверки правильности имени продукта на первой и второй страницах
print("INFO cart product #1 GOOD")

cart_price_product_1 = driver.find_element(by=By.XPATH, value="//div[@class='inventory_item_price']")
cart_value_price_product_1 = cart_price_product_1.text #сохраняем в переменную название продукта
print(cart_value_price_product_1)
assert cart_value_price_product_1 == value_price_product_1 # нужны asserts для проверки правильности цены продукта на первой и второй страницах
print("INFO price product #1 GOOD")
# названия товаров и ценник бьются после выполнения кода выше, важно чтобы значиения на одной странице и на второй для названия и цены товара не отличались

"""Transfer to checkout page"""
checkout = driver.find_element(by=By.XPATH, value="//button[@id='checkout']")
checkout.click()
print("click checkout")

"""Insert personal user information"""
first_name = driver.find_element(by=By.XPATH, value="//input[@id='first-name']")
first_name.send_keys("Igor")
print("First name is entered")

last_name = driver.find_element(by=By.XPATH, value="//input[@id='last-name']")
last_name.send_keys("Smith")
print("Last name is entered")

postal_code = driver.find_element(by=By.XPATH, value="//input[@id='postal-code']")
postal_code.send_keys("247500")
print("Postal code is entered")

"""Continue to payment"""
continue_button = driver.find_element(by=By.XPATH, value="//input[@id='continue']")
continue_button.click()
print("continue is clicked")

"""Verification of 'Checkout: Overview' page"""
checkout_overview = 'Checkout: Overview'
find_checkout_overview = driver.find_element(by=By.XPATH, value="//span[@class='title']")
find_checkout_overview_name = find_checkout_overview.text
assert find_checkout_overview_name == checkout_overview
print("We are on 'Checkout: Overview' page")

"""INFO Overview product #1"""
overview_product_1 = driver.find_element(by=By.XPATH, value="//div[@class='inventory_item_name']")
overview_value_product_1 = overview_product_1.text #сохраняем в переменную название продукта
print(overview_value_product_1)
assert overview_value_product_1 == value_product_1 # нужны asserts для проверки правильности имени продукта на первой и второй страницах
print("INFO overview product #1 GOOD")

overview_price_product_1 = driver.find_element(by=By.XPATH, value="//div[@class='inventory_item_price']")
overview_value_price_product_1 = overview_price_product_1.text #сохраняем в переменную название продукта
print(overview_value_price_product_1)
assert overview_value_price_product_1 == value_price_product_1 # нужны asserts для проверки правильности цены продукта на первой и второй страницах
print("INFO overview price product #1 GOOD")

total_price = driver.find_element(by=By.XPATH, value="//div[@class='summary_subtotal_label']")
total_price_value = total_price.text
print(total_price_value)

# нам нужно из всего текста Item total: $29.99 только $29.99, поэтому создим переменную, кот ищет только цену
item_total = f'Item total: {value_price_product_1}' #вставляем в фиг скобках переменную, а не цифру, чтоб в случае если цена поменяется тест не падал
print(item_total)
assert item_total == total_price_value
print("total overview price is Good")

finish = driver.find_element(by=By.XPATH, value="//button[@id='finish']")
finish.click()

"""Verification of 'Checkout: Overview' page"""
checkout_overview = 'Checkout: Overview'
find_checkout_overview = driver.find_element(by=By.XPATH, value="//span[@class='title']")
find_checkout_overview_name = find_checkout_overview.text
assert find_checkout_overview_name == checkout_overview
print("We are on 'Checkout: Overview' page")




