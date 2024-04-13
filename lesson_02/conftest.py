import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import data
from locators import MainPage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver 
    print('\nquit browser...')
    driver.quit()
    

@pytest.fixture()
def authorize(driver):
    driver.get(data.url)
    driver.find_element(By.XPATH, MainPage.username_field).send_keys(data.login)
    driver.find_element(By.XPATH, MainPage.password_field).send_keys(data.password)
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, MainPage.login_button).click()