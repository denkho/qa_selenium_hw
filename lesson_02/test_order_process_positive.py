from selenium import webdriver
from selenium.webdriver.common.by import By
import time



url = 'https://www.saucedemo.com/'
url_inventory = 'https://www.saucedemo.com/inventory.html'
url_cart = 'https://www.saucedemo.com/cart.html'
login = 'standard_user'
password = 'secret_sauce'
first_name = 'Mark'
last_name = 'Zimmerman'
zip = '123456'
complete_header = 'Thank you for your order!'


def test_order_positive():
    driver = webdriver.Chrome()
    
    driver.get(url)
    time.sleep(2)

    # authorization 
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(login)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(5)

    # adding item to the cart
    item_name = driver.find_element(By.XPATH, '//*[@data-test="inventory-item-name"]').text
    item_name_prepared = '-'.join(item_name.lower().split())
    item_name_for_cart_id = '//*[@data-test="add-to-cart-' + item_name_prepared + '"]'
    
    driver.find_element(By.XPATH, item_name_for_cart_id).click()
    time.sleep(5)

    # go to cart
    driver.get(url_cart)
    time.sleep(5)

    driver.find_element(By.XPATH, '//button[@data-test="checkout"]').click()
    time.sleep(5)

    # input name and zip
    driver.find_element(By.XPATH, '//*[@data-test="firstName"]').send_keys(first_name)
    driver.find_element(By.XPATH, '//*[@data-test="lastName"]').send_keys(last_name)
    driver.find_element(By.XPATH, '//*[@data-test="postalCode"]').send_keys(zip)
    time.sleep(5)

    driver.find_element(By.XPATH, '//input[@data-test="continue"]').click()
    time.sleep(5)

    # checkout step 2
    driver.find_element(By.XPATH, '//button[@data-test="finish"]').click()
    time.sleep(5)

    assert driver.find_element(By.XPATH, '//*[@data-test="complete-header"]').text == complete_header


    driver.quit()


