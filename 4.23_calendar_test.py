import datetime

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()

"""Clear input date field"""
new_date = driver.find_element(by=By.XPATH, value="//input[@id='datePickerMonthYearInput']")
new_date.click()
new_date.send_keys(Keys.BACKSPACE*10)

"""Create 10 days later date than current"""
current_date_10 = datetime.datetime.utcnow() + datetime.timedelta(days=10)
current_date_needed_format = current_date_10.strftime("%m/%d/%Y")
print(current_date_needed_format)

"""Insert 10 days later date into input date field"""
new_date.send_keys(current_date_needed_format)

"""Save screenshot"""
current_date = datetime.datetime.utcnow().strftime("%d.%m.%Y.%H.%M.%S")
screenshot_name = f'screenshot_test_calendar_{current_date}.png'
driver.save_screenshot("C:\\Users\\Просто юзер\\PycharmProjects\\python_selenium\\Screenshots\\" + screenshot_name)

new_date.send_keys(Keys.RETURN)





