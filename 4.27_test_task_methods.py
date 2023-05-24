from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import constant

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

"""Login"""
login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(by=By.XPATH, value="//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("input login")
password = driver.find_element(by=By.XPATH, value="//input[@id='password']")
password.send_keys(password_all)
print("input password")
password.send_keys(Keys.RETURN)

print("Приветствуем вас на сайте нашего интернет магазина!")
print("Выберите один из следующих товаров и введите его номер для покупки: 1 - Sauce Labs Backpack, 2 - Sauce Labs Bike Light, "
      "3 - Sauce Labs Bolt T-Shirt, 4 - Sauce Labs Fleece Jacket, 5 - Sauce Labs Onesie, 6 - T-Shirt (Red)")
product = input()
print(product)

if product == "1":
    """INFO product #1"""
    product_1 = driver.find_element(by=By.XPATH, value="//a[@id='item_4_title_link']")
    value_product_1 = product_1.text
    print(value_product_1)

    price_product_1 = driver.find_element(by=By.XPATH, value="//div[@class='inventory_item_price']")
    value_price_product_1 = price_product_1.text
    print(value_price_product_1)

    """Add product_1 to cart"""
    select_product_1 = driver.find_element(by=By.XPATH, value="//button[@id='add-to-cart-sauce-labs-backpack']")
    select_product_1.click()
    print("product 1 is added to cart")

    """Transfer to the cart"""
    constant.transfer_to_cart()

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

    """Check total price for item 1"""
    total_price_1 = driver.find_element(by=By.XPATH, value="//div[@class='summary_subtotal_label']")
    total_price_value_1 = total_price_1.text
    print(total_price_value_1)

    item_1_total = f'Item total: {value_price_product_1}'
    print(item_1_total)
    assert item_1_total == total_price_value_1
    print("total overview price is Good")

    """Finish button click"""
    finish = driver.find_element(by=By.XPATH, value="//button[@id='finish']")
    finish.click()

elif product == "2":
    """INFO product #2"""
    product_2 = driver.find_element(by=By.XPATH, value="//a[@id='item_0_title_link']")
    value_product_2 = product_2.text
    print(value_product_2)

    price_product_2 = driver.find_element(by=By.XPATH, value="//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
    value_price_product_2 = price_product_2.text
    print(value_price_product_2)

    """Add product_2 to cart"""
    select_product_2 = driver.find_element(by=By.XPATH, value="//button[@id='add-to-cart-sauce-labs-bike-light']")
    select_product_2.click()
    print("product 2 is added to cart")

    """Transfer to the cart"""
    cart = driver.find_element(by=By.XPATH, value="//a[@class='shopping_cart_link']")
    cart.click()
    print("Transfer to the cart")

    """INFO cart product #2"""
    cart_product_2 = driver.find_element(by=By.XPATH, value="//a[@id='item_0_title_link']")
    cart_value_product_2 = cart_product_2.text
    print(cart_value_product_2)
    assert cart_value_product_2 == value_product_2
    print("INFO cart product #2 GOOD")

    cart_price_product_2 = driver.find_element(by=By.XPATH, value="//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
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

    """INFO Overview product #2"""
    overview_product_2 = driver.find_element(by=By.XPATH, value="//a[@id='item_0_title_link']")
    overview_value_product_2 = overview_product_2.text
    print(overview_value_product_2)
    assert overview_value_product_2 == value_product_2
    print("INFO overview product #2 is GOOD")

    overview_price_product_2 = driver.find_element(by=By.XPATH, value="//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
    overview_value_price_product_2 = overview_price_product_2.text
    print(overview_value_price_product_2)
    assert overview_value_price_product_2 == value_price_product_2
    print("INFO overview price product #2 is GOOD")

    """Check total price for item 2"""
    total_price_2 = driver.find_element(by=By.XPATH, value="//div[@class='summary_subtotal_label']")
    total_price_value_2 = total_price_2.text
    print(total_price_value_2)

    item_2_total = f'Item total: {value_price_product_2}'
    print(item_2_total)
    assert item_2_total == total_price_value_2
    print("total overview price is Good")

    """Finish button click"""
    finish = driver.find_element(by=By.XPATH, value="//button[@id='finish']")
    finish.click()

elif product == "3":
    """INFO product #3"""
    product_3 = driver.find_element(by=By.XPATH, value="//a[@id='item_1_title_link']")
    value_product_3 = product_3.text
    print(value_product_3)

    price_product_3 = driver.find_element(by=By.XPATH, value="//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div")
    value_price_product_3 = price_product_3.text
    print(value_price_product_3)

    """Add product_3 to cart"""
    select_product_3 = driver.find_element(by=By.XPATH, value="//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
    select_product_3.click()
    print("product 3 is added to cart")

    """Transfer to the cart"""
    cart = driver.find_element(by=By.XPATH, value="//a[@class='shopping_cart_link']")
    cart.click()
    print("Transfer to the cart")

    """INFO cart product #3"""
    cart_product_3 = driver.find_element(by=By.XPATH, value="//a[@id='item_5_title_link']")
    cart_value_product_3 = cart_product_3.text
    print(cart_value_product_3)
    assert cart_value_product_3 == value_product_3
    print("INFO cart product #3 GOOD")

    cart_price_product_3 = driver.find_element(by=By.XPATH, value="//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
    cart_value_price_product_3 = cart_price_product_3.text
    print(cart_value_price_product_3)
    assert cart_value_price_product_3 == value_price_product_3
    print("INFO price product #3 GOOD")

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

    """INFO Overview product #3"""
    overview_product_3 = driver.find_element(by=By.XPATH, value="//*[@id='item_1_title_link']")
    overview_value_product_3 = overview_product_3.text
    print(overview_value_product_3)
    assert overview_value_product_3 == value_product_3
    print("INFO overview product #3 is GOOD")

    overview_price_product_3 = driver.find_element(by=By.XPATH, value="//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
    overview_value_price_product_3 = overview_price_product_3.text
    print(overview_value_price_product_3)
    assert overview_value_price_product_3 == value_price_product_3
    print("INFO overview price product #3 is GOOD")

    """Check total price for item 3"""
    total_price_3 = driver.find_element(by=By.XPATH, value="//div[@class='summary_subtotal_label']")
    total_price_value_3 = total_price_3.text
    print(total_price_value_3)

    item_3_total = f'Item total: {value_price_product_3}'
    print(item_3_total)
    assert item_3_total == total_price_value_3
    print("total overview price is Good")

    """Finish button click"""
    finish = driver.find_element(by=By.XPATH, value="//button[@id='finish']")
    finish.click()

elif product == "4":
    """INFO product #4"""
    product_4 = driver.find_element(by=By.XPATH, value="//a[@id='item_5_title_link']")
    value_product_4 = product_4.text
    print(value_product_4)

    price_product_4 = driver.find_element(by=By.XPATH, value="//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div")
    value_price_product_4 = price_product_4.text
    print(value_price_product_4)

    """Add product_4 to cart"""
    select_product_4 = driver.find_element(by=By.XPATH, value="//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
    select_product_4.click()
    print("product 4 is added to cart")

    """Transfer to the cart"""
    cart = driver.find_element(by=By.XPATH, value="//a[@class='shopping_cart_link']")
    cart.click()
    print("Transfer to the cart")

    """INFO cart product #4"""
    cart_product_4 = driver.find_element(by=By.XPATH, value="//a[@id='item_5_title_link']")
    cart_value_product_4 = cart_product_4.text
    print(cart_value_product_4)
    assert cart_value_product_4 == value_product_4
    print("INFO cart product #4 GOOD")

    cart_price_product_4 = driver.find_element(by=By.XPATH, value="//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
    cart_value_price_product_4 = cart_price_product_4.text
    print(cart_value_price_product_4)
    assert cart_value_price_product_4 == value_price_product_4
    print("INFO price product #4 GOOD")

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

    """INFO Overview product #4"""
    overview_product_4 = driver.find_element(by=By.XPATH, value="//a[@id='item_5_title_link']")
    overview_value_product_4 = overview_product_4.text
    print(overview_value_product_4)
    assert overview_value_product_4 == value_product_4
    print("INFO overview product #4 is GOOD")

    overview_price_product_4 = driver.find_element(by=By.XPATH, value="//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
    overview_value_price_product_4 = overview_price_product_4.text
    print(overview_value_price_product_4)
    assert overview_value_price_product_4 == value_price_product_4
    print("INFO overview price product #4 is GOOD")

    """Check total price for item 4"""
    total_price_4 = driver.find_element(by=By.XPATH, value="//div[@class='summary_subtotal_label']")
    total_price_value_4 = total_price_4.text
    print(total_price_value_4)

    item_4_total = f'Item total: {value_price_product_4}'
    print(item_4_total)
    assert item_4_total == total_price_value_4
    print("total overview price is Good")

    """Finish button click"""
    finish = driver.find_element(by=By.XPATH, value="//button[@id='finish']")
    finish.click()

elif product == "5":
    """INFO product #5"""
    product_5 = driver.find_element(by=By.XPATH, value="//a[@id='item_2_title_link']")
    value_product_5 = product_5.text
    print(value_product_5)

    price_product_5 = driver.find_element(by=By.XPATH, value="//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div")
    value_price_product_5 = price_product_5.text
    print(value_price_product_5)

    """Add product_5 to cart"""
    select_product_5 = driver.find_element(by=By.XPATH, value="//button[@id='add-to-cart-sauce-labs-onesie']")
    select_product_5.click()
    print("product 5 is added to cart")

    """Transfer to the cart"""
    cart = driver.find_element(by=By.XPATH, value="//a[@class='shopping_cart_link']")
    cart.click()
    print("Transfer to the cart")

    """INFO cart product #5"""
    cart_product_5 = driver.find_element(by=By.XPATH, value="//a[@id='item_2_title_link']")
    cart_value_product_5 = cart_product_5.text
    print(cart_value_product_5)
    assert cart_value_product_5 == value_product_5
    print("INFO cart product #5 GOOD")

    cart_price_product_5 = driver.find_element(by=By.XPATH, value="//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
    cart_value_price_product_5 = cart_price_product_5.text
    print(cart_value_price_product_5)
    assert cart_value_price_product_5 == value_price_product_5
    print("INFO price product #5 GOOD")

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

    """INFO Overview product #5"""
    overview_product_5 = driver.find_element(by=By.XPATH, value="//a[@id='item_2_title_link']")
    overview_value_product_5 = overview_product_5.text
    print(overview_value_product_5)
    assert overview_value_product_5 == value_product_5
    print("INFO overview product #5 is GOOD")

    overview_price_product_5 = driver.find_element(by=By.XPATH, value="//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
    overview_value_price_product_5 = overview_price_product_5.text
    print(overview_value_price_product_5)
    assert overview_value_price_product_5 == value_price_product_5
    print("INFO overview price product #5 is GOOD")

    """Check total price for item 5"""
    total_price_5 = driver.find_element(by=By.XPATH, value="//div[@class='summary_subtotal_label']")
    total_price_value_5 = total_price_5.text
    print(total_price_value_5)

    item_5_total = f'Item total: {value_price_product_5}'
    print(item_5_total)
    assert item_5_total == total_price_value_5
    print("total overview price is Good")

    """Finish button click"""
    finish = driver.find_element(by=By.XPATH, value="//button[@id='finish']")
    finish.click()

elif product == "6":
    """INFO product #6"""
    product_6 = driver.find_element(by=By.XPATH, value="//a[@id='item_3_title_link']")
    value_product_6 = product_6.text
    print(value_product_6)

    price_product_6 = driver.find_element(by=By.XPATH, value="//*[@id='inventory_container']/div/div[6]/div[2]/div[2]/div")
    value_price_product_6 = price_product_6.text
    print(value_price_product_6)

    """Add product_6 to cart"""
    select_product_6 = driver.find_element(by=By.XPATH, value="//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
    select_product_6.click()
    print("product 6 is added to cart")

    """Transfer to the cart"""
    cart = driver.find_element(by=By.XPATH, value="//a[@class='shopping_cart_link']")
    cart.click()
    print("Transfer to the cart")

    """INFO cart product #6"""
    cart_product_6 = driver.find_element(by=By.XPATH, value="//a[@id='item_3_title_link']")
    cart_value_product_6 = cart_product_6.text
    print(cart_value_product_6)
    assert cart_value_product_6 == value_product_6
    print("INFO cart product #6 GOOD")

    cart_price_product_6 = driver.find_element(by=By.XPATH, value="//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
    cart_value_price_product_6 = cart_price_product_6.text
    print(cart_value_price_product_6)
    assert cart_value_price_product_6 == value_price_product_6
    print("INFO price product #6 GOOD")

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

    """INFO Overview product #6"""
    overview_product_6 = driver.find_element(by=By.XPATH, value="//a[@id='item_3_title_link']")
    overview_value_product_6 = overview_product_6.text
    print(overview_value_product_6)
    assert overview_value_product_6 == value_product_6
    print("INFO overview product #6 is GOOD")

    overview_price_product_6 = driver.find_element(by=By.XPATH, value="//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
    overview_value_price_product_6 = overview_price_product_6.text
    print(overview_value_price_product_6)
    assert overview_value_price_product_6 == value_price_product_6
    print("INFO overview price product #6 is GOOD")

    """Check total price for item 6"""
    total_price_6 = driver.find_element(by=By.XPATH, value="//div[@class='summary_subtotal_label']")
    total_price_value_6 = total_price_6.text
    print(total_price_value_6)

    item_6_total = f'Item total: {value_price_product_6}'
    print(item_6_total)
    assert item_6_total == total_price_value_6
    print("total overview price is Good")

    """Finish button click"""
    finish = driver.find_element(by=By.XPATH, value="//button[@id='finish']")
    finish.click()

else:
    print("Вы ввели несуществующий номер товара. Введите один из указанных номеров товаров.")



