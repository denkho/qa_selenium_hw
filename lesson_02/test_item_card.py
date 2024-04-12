from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


url = 'https://www.saucedemo.com/'
url_inventory = 'https://www.saucedemo.com/inventory.html'
url_cart = 'https://www.saucedemo.com/cart.html'
login = 'standard_user'
password = 'secret_sauce'


def authorization():
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(login)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()


def test_positive_go_to_item_card_page_from_inventory_item_image():
    driver.get(url)

    authorization()

    item_name = driver.find_element(By.XPATH, '//*[@data-test="inventory-item-name"]').text
    item_name_prepared = '-'.join(item_name.lower().split())
    img_xpath = '//*[@data-test="inventory-item-' + item_name_prepared + '-img"]'
    driver.find_element(By.XPATH, img_xpath).click()
    time.sleep(3)

    assert driver.find_element(By.XPATH, '//*[@data-test="inventory-item-name"]').text == item_name




def test_positive_go_to_item_card_page_from_inventory_item_title():
    driver.get(url)

    authorization()

    item_name = driver.find_element(By.XPATH, '//*[@data-test="inventory-item-name"]').text
    driver.find_element(By.XPATH, '//*[@data-test="inventory-item-name"]').click()
    time.sleep(3)

    assert driver.find_element(By.XPATH, '//*[@data-test="inventory-item-name"]').text == item_name