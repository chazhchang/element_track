# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import datetime
import time
import winsound

ALARM_BEEP_DURATION = 1000  # milliseconds
ALARM_FREQ = 440  # Hz
ALARM_DURATION = 5  # 2n sec
firefox_profile_path = r'C:\Users\Justin\AppData\Roaming\Mozilla\Firefox\Profiles\j4e948dv.default-release'
# url = 'https://www.bestbuy.com/site/amd-ryzen-5-5600x-4th-gen-6-core-12-threads-unlocked-desktop-processor-with-wraith-stealth-cooler/6438943.p?skuId=6438943'
# url = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402'
# url = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442'
url = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-ti-8gb-gddr6x-pci-express-4-0-graphics-card-dark-platinum-and-black/6465789.p?skuId=6465789'
# url = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440'

# options = Options()
# options.headless = True
# driver = webdriver.Firefox(options=options)
profile = webdriver.FirefoxProfile(firefox_profile_path)
driver = webdriver.Firefox(firefox_profile=profile)

driver.get(url)

while True:
    add_to_cart_but = WebDriverWait(driver, 3600).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.add-to-cart-button')))
    
    if 'btn-disabled' in add_to_cart_but.get_attribute("class"):
        time.sleep(2)
        driver.refresh()
    else:
        break

# add_on_checkbox = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, 'add-on-selector-add-on-item-checkbox')))
# add_on_checkbox.click()

add_to_cart_but = WebDriverWait(driver, 3600).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.add-to-cart-button')))
print(add_to_cart_but.value_of_css_property('background-color'))
add_to_cart_but.click()

print('1st Add to Cart button clicked. In Queue.', datetime.datetime.now())
time.sleep(5)
print(add_to_cart_but.value_of_css_property('background-color'))

while True:
    # add_to_cart_but = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, '.add-to-cart-button')))
    please_wait_enabled = add_to_cart_but.value_of_css_property('background-color')

    if please_wait_enabled == 'rgb(197, 203, 213)':
        time.sleep(0.05)
    else:
        break

add_to_cart_but = WebDriverWait(driver, 3600).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.add-to-cart-button')))
add_to_cart_but.click()

print('2nd Add to Cart button clicked. Item added to Cart', datetime.datetime.now())
print(add_to_cart_but.value_of_css_property('background-color'))

for _ in range(ALARM_DURATION):
    winsound.Beep(ALARM_FREQ, ALARM_BEEP_DURATION)
    time.sleep(1)
