from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
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


def check_exist_element(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return True
    return False


def add_item_to_cart_from_inventory():
    item_name = driver.find_element(By.XPATH, '//*[@data-test="inventory-item-name"]').text
    item_name_prepared = '-'.join(item_name.lower().split())
    item_name_for_cart_id = '//*[@data-test="add-to-cart-' + item_name_prepared + '"]'
    
    driver.find_element(By.XPATH, item_name_for_cart_id).click()
    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@data-test="shopping-cart-link"]').click()
    time.sleep(2)
    return item_name_prepared


def test_add_item_to_cart_from_inventory():
    driver.get(url)

    authorization()
    time.sleep(1)

    item_name = driver.find_element(By.XPATH, '//*[@data-test="inventory-item-name"]').text
    item_name_prepared = '-'.join(item_name.lower().split())
    item_name_for_cart_id = '//*[@data-test="add-to-cart-' + item_name_prepared + '"]'
    
    driver.find_element(By.XPATH, item_name_for_cart_id).click()
    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@data-test="shopping-cart-link"]').click()
    time.sleep(2)
    
    assert driver.find_element(By.XPATH, '//*[@data-test="inventory-item-name"]').text == item_name
    


def test_delete_item_from_cart():
    driver.get(url)

    authorization()
    time.sleep(1)
    item_name_prepared = add_item_to_cart_from_inventory()
    item_name_for_remove_cart_id = '//*[@data-test="remove-' + item_name_prepared + '"]'
    
    driver.get(url_cart)
    driver.find_element(By.XPATH, item_name_for_remove_cart_id).click()
    
    assert check_exist_element('//*[@data-test="inventory-item-name"]') == True
    





