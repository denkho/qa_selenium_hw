from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


url = 'https://www.saucedemo.com/'
url_inventory = 'https://www.saucedemo.com/inventory.html'
url_cart = 'https://www.saucedemo.com/cart.html'
url_about = 'https://saucelabs.com/'
login = 'standard_user'
password = 'secret_sauce'


def test_burger_menu_logout():
    driver = webdriver.Chrome()
    
    driver.get(url)
    time.sleep(2)

    # authorization 
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(login)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(2)

    # logout test
    driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, 'Logout').click()

    time.sleep(2)

    assert driver.current_url == url

    driver.quit()


def test_burger_about_button():
    driver = webdriver.Chrome()
    
    driver.get(url)
    time.sleep(2)

    # authorization 
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(login)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(2)

    # logout test
    driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, 'About').click()

    time.sleep(3)

    assert driver.current_url == url_about

    driver.quit()


def xpath_transformator_to_cart_button(item_name):
    item_name_prepared = '-'.join(item_name.lower().split())
    item_name_for_cart_id = '//*[@data-test="add-to-cart-' + item_name_prepared + '"]'
    return item_name_for_cart_id






def test_burger_reset_app():
    driver = webdriver.Chrome()
    
    driver.get(url)
    time.sleep(2)

    # authorization 
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(login)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(2)


    elements_in_inventory = driver.find_elements(By.XPATH, '//*[@data-test="inventory-item-name"]')
    elements_in_inventory = [element.text for element in elements_in_inventory]

    ids_to_cart_add = [xpath_transformator_to_cart_button(elem) for elem in elements_in_inventory]

    for one_id in ids_to_cart_add:
        driver.find_element(By.XPATH, one_id).click()
    
    time.sleep(2)
    driver.get(url_cart)
    time.sleep(2)

    # reset app test
    driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click()
    time.sleep(2)
    
    driver.find_element(By.LINK_TEXT, 'Reset App State').click()
    time.sleep(2)
    
    try:
        driver.find_element(By.XPATH, '//*[@data-test="inventory-item-name"]')
    except NoSuchElementException:
        assert 0 == 0    

    driver.quit()
