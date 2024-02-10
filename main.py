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
break_timeout = time.time() + 300
while True:
    if time.time() > timeout:
        store = driver.find_element(By.ID, 'store')
        perks = [perk for perk in store.find_elements(By.TAG_NAME, 'div')[:-1]][::-1]
        for perk in perks:
            if perk.get_attribute('class') != 'grayed':
                perk.click()
                timeout = time.time() + 5
                break
    if time.time() > break_timeout:
        print(driver.find_element(By.ID, 'cps').text)
        break
    cookie.click()
