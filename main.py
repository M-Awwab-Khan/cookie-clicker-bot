from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.ID, 'cookie')
timeout = time.time() + 5
store = driver.find_element(By.ID, 'store')
prices = [int(price.text.split(' - ')[1].replace(',', '')) for price in store.find_elements(By.TAG_NAME, 'b')[:-1]]
prices.reverse()
perks = [perk for perk in store.find_elements(By.TAG_NAME, 'div')[:-1]]
perks.reverse()
prices_perks = zip(prices, perks)

while True:
    if time.time() > timeout:
        for price, perk in prices_perks:
            if int(driver.find_element(By.ID, 'money').text) > price:
                perk.click()
                timeout = time.time() + 5
                break
    cookie.click()
