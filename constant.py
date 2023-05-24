from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)

"""Transfer to the cart"""
def transfer_to_cart():
    cart = driver.find_element(by=By.XPATH, value="//a[@class='shopping_cart_link']")
    cart.click()
    print("Transfer to the cart")

