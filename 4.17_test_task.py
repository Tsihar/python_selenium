import datetime

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
driver.maximize_window()

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
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(by=By.XPATH, value="//div[@class='inventory_item_price']")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

"""INFO product #2"""
product_2 = driver.find_element(by=By.XPATH, value="//a[@id='item_0_title_link']")
value_product_2 = product_2.text
print(value_product_2)

price_product_2 = driver.find_element(by=By.XPATH, value="//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
value_price_product_2 = price_product_2.text
print(value_price_product_2)

"""Add product_1 to cart"""
select_product_1 = driver.find_element(by=By.XPATH, value="//button[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print("product 1 is added to cart")

"""Add product_2 to cart"""
select_product_2 = driver.find_element(by=By.XPATH, value="//button[@id='add-to-cart-sauce-labs-bike-light']")
select_product_2.click()
print("product 2 is added to cart")

"""Transfer to the cart"""
cart = driver.find_element(by=By.XPATH, value="//a[@class='shopping_cart_link']")
cart.click()
print("Transfer to the cart")

"""INFO cart product #1"""
cart_product_1 = driver.find_element(by=By.XPATH, value="//a[@id='item_4_title_link']")
cart_value_product_1 = cart_product_1.text
print(cart_value_product_1)
assert cart_value_product_1 == value_product_1
print("INFO cart product #1 GOOD")

cart_price_product_1 = driver.find_element(by=By.XPATH, value="//div[@class='inventory_item_price']")
cart_value_price_product_1 = cart_price_product_1.text
print(cart_value_price_product_1)
assert cart_value_price_product_1 == value_price_product_1
print("INFO price product #1 GOOD")

"""INFO cart product #2"""
cart_product_2 = driver.find_element(by=By.XPATH, value="//a[@id='item_0_title_link']")
cart_value_product_2 = cart_product_2.text
print(cart_value_product_2)
assert cart_value_product_2 == value_product_2
print("INFO cart product #2 GOOD")

cart_price_product_2 = driver.find_element(by=By.XPATH, value="//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
cart_value_price_product_2 = cart_price_product_2.text
print(cart_value_price_product_2)
assert cart_value_price_product_2 == value_price_product_2
print("INFO price product #2 GOOD")

"""Transfer to checkout page"""
checkout = driver.find_element(by=By.XPATH, value="//button[@id='checkout']")
checkout.click()
print("click checkout")

"""Insert personal user information"""
first_name = driver.find_element(by=By.XPATH, value="//input[@id='first-name']")
first_name.send_keys("Igor")
print("First name is entered")

last_name = driver.find_element(by=By.XPATH, value="//input[@id='last-name']")
last_name.send_keys("T")
print("Last name is entered")

postal_code = driver.find_element(by=By.XPATH, value="//input[@id='postal-code']")
postal_code.send_keys("123456")
print("Postal code is entered")

"""Continue to payment"""
continue_button = driver.find_element(by=By.XPATH, value="//input[@id='continue']")
continue_button.click()
print("continue is clicked")


"""INFO Overview product #1"""
overview_product_1 = driver.find_element(by=By.XPATH, value="//div[@class='inventory_item_name']")
overview_value_product_1 = overview_product_1.text
print(overview_value_product_1)
assert overview_value_product_1 == value_product_1
print("INFO overview product #1 GOOD")

overview_price_product_1 = driver.find_element(by=By.XPATH, value="//div[@class='inventory_item_price']")
overview_value_price_product_1 = overview_price_product_1.text
print(overview_value_price_product_1)
assert overview_value_price_product_1 == value_price_product_1
print("INFO overview price product #1 GOOD")

"""INFO Overview product #2"""
overview_product_2 = driver.find_element(by=By.XPATH, value="//a[@id='item_0_title_link']")
overview_value_product_2 = overview_product_2.text
print(overview_value_product_2)
assert overview_value_product_2 == value_product_2
print("INFO overview product #2 is GOOD")

overview_price_product_2 = driver.find_element(by=By.XPATH, value="//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
overview_value_price_product_2 = overview_price_product_2.text
print(overview_value_price_product_2)
assert overview_value_price_product_2 == value_price_product_2
print("INFO overview price product #2 is GOOD")

"""Check total price and sign '$' removal"""
value_price_product_1_without_dollar = float(value_price_product_1.replace("$", ""))
print(value_price_product_1_without_dollar)
value_price_product_2_without_dollar = float(value_price_product_2.replace("$", ""))
print(value_price_product_2_without_dollar)

total_price = driver.find_element(by=By.XPATH, value="//div[@class='summary_subtotal_label']")
total_price_value = total_price.text
print(total_price_value)

item_total = f'Item total: ${value_price_product_1_without_dollar + value_price_product_2_without_dollar}'
print(item_total)
assert item_total == total_price_value
print("total overview price is correct")

"""Finish button click"""
finish = driver.find_element(by=By.XPATH, value="//button[@id='finish']")
finish.click()

"""Verification of 'Checkout: Complete!' page"""
checkout_complete_text = 'Checkout: Complete!'
checkout_complete_page = driver.find_element(by=By.XPATH, value="//*[@id='header_container']/div[2]/span")
checkout_complete_page_name = checkout_complete_page.text
assert checkout_complete_page_name == checkout_complete_text
print("We are on 'Checkout: Complete!' page")

current_date = datetime.datetime.utcnow().strftime("%d.%m.%Y.%H.%M.%S")
items_purchase = f'items_purchase_{current_date}.png'
driver.save_screenshot("C:\\Users\\Просто юзер\\PycharmProjects\\python_selenium\\Screenshots\\" + items_purchase)




