# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import datetime
import time

firefox_profile_path = r'C:\Users\WebUser\AppData\Roaming\Mozilla\Firefox\Profiles\7yqdk170.default'
url = 'https://www.bestbuy.com/site/amd-ryzen-5-5600x-4th-gen-6-core-12-threads-unlocked-desktop-processor-with-wraith-stealth-cooler/6438943.p?skuId=6438943'
# url = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402'

# options = Options()
# options.headless = True
# driver = webdriver.Firefox(options=options)
profile = webdriver.FirefoxProfile(firefox_profile_path)
driver = webdriver.Firefox(firefox_profile=profile)

driver.get(url)

while True:
    add_to_cart_but = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.add-to-cart-button')))
    
    if 'btn-disabled' in add_to_cart_but.get_attribute("class"):
        time.sleep(5)
        driver.refresh()
    else:
        break

# add_on_checkbox = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, 'add-on-selector-add-on-item-checkbox')))
# add_on_checkbox.click()

add_to_cart_but = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.add-to-cart-button')))
add_to_cart_but.click()

print('1st Add to Cart button clicked. In Queue')
time.sleep(5)

while True:
    add_to_cart_but = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.add-to-cart-button')))
    please_wait_enabled = add_to_cart_but.get_attribute('aria-describedby')

    if please_wait_enabled:
        time.sleep(0.1)
    else:
        break

add_to_cart_but = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.add-to-cart-button')))
add_to_cart_but.click()

print('2nd Add to Cart button clicked. In Queue')
