from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://www.saucedemo.com/'
url_inventory = 'https://www.saucedemo.com/inventory.html'
login = 'standard_user'
password = 'secret_sauce'
login_negative = 'user'
password_negative = 'user'

def test_authorisation_with_positive_credentials():
    driver.get(url)

    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(login)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

    assert driver.current_url == url_inventory, 'URL is incorrect'

def test_authorisation_with_negative_credentials():
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(login_negative)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password_negative)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

    assert driver.find_element(By.XPATH, '//*[@data-test="error"]').text == 'Epic sadface: Username and password do not match any user in this service'