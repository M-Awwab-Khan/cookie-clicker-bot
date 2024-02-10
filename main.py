from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.ID, 'cookie')
money = driver.find_element(By.ID, 'money')
# timeout = time.time() + 60*5
store = driver.find_element(By.ID, 'store')
prices = [int(price.split('-')[1].strip()) for price in store.find_elements(By.TAG_NAME, 'b')]
perks = [perk for perk in store.find_elements(By.TAG_NAME, 'div')]
prices_perks = zip(prices, perks)

# while True:
#     if time.time() > timeout:

#     cookie.click()


