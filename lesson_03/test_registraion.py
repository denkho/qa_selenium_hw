from data import Credentials, Messages, Urls
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


def test_registration_explicit_waits(driver, wait):
    driver.get(Urls.url)
    wait.until(EC.element_to_be_clickable(Locators.button_start))
    driver.find_element(*Locators.button_start).click()

    driver.find_element(*Locators.login_field).send_keys(Credentials.login)
    driver.find_element(*Locators.password_field).send_keys(Credentials.password)

    driver.find_element(*Locators.checkbox_agree).click()
    driver.find_element(*Locators.button_register).click()

    wait.until(EC.visibility_of_element_located(Locators.message_success))

    assert driver.find_element(*Locators.message_success).text == Messages.success