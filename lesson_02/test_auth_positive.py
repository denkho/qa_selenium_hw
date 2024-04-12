from selenium.webdriver.common.by import By

import data
from locators import MainPage

def test_authorisation_with_positive_credentials(driver):
    driver.get(data.url)

    driver.find_element(By.XPATH, MainPage.username_field).send_keys(data.login)
    driver.find_element(By.XPATH, MainPage.password_field).send_keys(data.password)
    driver.find_element(By.XPATH, MainPage.login_button).click()

    assert driver.current_url == data.url_inventory, 'URL is incorrect'


def test_authorisation_with_negative_credentials(driver):
    driver.get(data.url)
    driver.find_element(By.XPATH, MainPage.username_field).send_keys(data.login_negative)
    driver.find_element(By.XPATH, MainPage.password_field).send_keys(data.password_negative)
    driver.find_element(By.XPATH, MainPage.login_button).click()

    assert driver.find_element(By.XPATH, MainPage.login_error_message).text == MainPage.login_error_message_text


