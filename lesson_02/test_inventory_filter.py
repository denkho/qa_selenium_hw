from selenium import webdriver
from selenium.webdriver.common.by import By
import time


url = 'https://www.saucedemo.com/'
url_inventory = 'https://www.saucedemo.com/inventory.html'
url_cart = 'https://www.saucedemo.com/cart.html'
login = 'standard_user'
password = 'secret_sauce'


def test_filter_A_Z():
    driver = webdriver.Chrome()
    
    driver.get(url)
    time.sleep(2)

    # authorization 
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(login)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(2)

    # sort inversed order 
    driver.find_element(By.XPATH, '//*[@data-test="product-sort-container"]').click()
    driver.find_element(By.XPATH, '//option[@value="za"]').click()
    time.sleep(2)

    
    # sort AZ to check 
    driver.find_element(By.XPATH, '//*[@data-test="product-sort-container"]').click()
    driver.find_element(By.XPATH, '//option[@value="az"]').click()
    time.sleep(2)

    # get list of names of all items
    elements = driver.find_elements(By.XPATH, '//*[@data-test="inventory-item-name"]')
    elements = [element.text for element in elements]

    elements_ordered = sorted(elements)

    assert elements == elements_ordered
    
    driver.quit()


def test_filter_Z_A():
    driver = webdriver.Chrome()
    
    driver.get(url)
    time.sleep(2)

    # authorization 
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(login)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(2)

    # sort inversed order 
    driver.find_element(By.XPATH, '//*[@data-test="product-sort-container"]').click()
    driver.find_element(By.XPATH, '//option[@value="az"]').click()
    time.sleep(2)

    
    # sort AZ to check 
    driver.find_element(By.XPATH, '//*[@data-test="product-sort-container"]').click()
    driver.find_element(By.XPATH, '//option[@value="za"]').click()
    time.sleep(2)

    # get list of names of all items
    elements = driver.find_elements(By.XPATH, '//*[@data-test="inventory-item-name"]')
    elements = [element.text for element in elements]

    elements_ordered = sorted(elements, reverse=True)

    assert elements == elements_ordered
    
    driver.quit()


def test_filter_Lo_High():
    driver = webdriver.Chrome()
    
    driver.get(url)
    time.sleep(2)

    # authorization 
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(login)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(2)

    # sort inversed order 
    driver.find_element(By.XPATH, '//*[@data-test="product-sort-container"]').click()
    driver.find_element(By.XPATH, '//option[@value="hilo"]').click()
    time.sleep(2)

    
    # sort Lo High to check 
    driver.find_element(By.XPATH, '//*[@data-test="product-sort-container"]').click()
    driver.find_element(By.XPATH, '//option[@value="lohi"]').click()
    time.sleep(2)

    # get list of names of all items
    elements = driver.find_elements(By.XPATH, '//*[@data-test="inventory-item-price"]')
    elements = [float(element.text[1:]) for element in elements]

    elements_ordered = sorted(elements)

    assert elements == elements_ordered
    
    driver.quit()

def test_filter_High_Lo():
    driver = webdriver.Chrome()
    
    driver.get(url)
    time.sleep(2)

    # authorization 
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(login)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(2)

    # sort inversed order 
    driver.find_element(By.XPATH, '//*[@data-test="product-sort-container"]').click()
    driver.find_element(By.XPATH, '//option[@value="lohi"]').click()
    time.sleep(2)

    
    # sort High Lo to check 
    driver.find_element(By.XPATH, '//*[@data-test="product-sort-container"]').click()
    driver.find_element(By.XPATH, '//option[@value="hilo"]').click()
    time.sleep(2)

    # get list of names of all items
    elements = driver.find_elements(By.XPATH, '//*[@data-test="inventory-item-price"]')
    elements = [float(element.text[1:]) for element in elements]

    elements_ordered = sorted(elements, reverse=True)

    assert elements == elements_ordered
    
    driver.quit()
