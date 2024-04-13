from selenium.webdriver.common.by import By

import data
from locators import Inventory, Cart, Order


def test_order_positive(driver, authorize):
    # adding item to the cart
    item_name = driver.find_element(By.XPATH, Inventory.element_name).text
    driver.find_element(By.XPATH, Cart.xpath_transformator_to_cart_button(item_name)).click()
    driver.implicitly_wait(2)

    # go to cart
    driver.get(data.url_cart)
    driver.implicitly_wait(2)

    driver.find_element(By.XPATH, Order.checkout_button).click()
    driver.implicitly_wait(2)

    # input name and zip
    driver.find_element(By.XPATH, Order.first_name_xpath).send_keys(data.first_name)
    driver.find_element(By.XPATH, Order.last_name_xpath).send_keys(data.last_name)
    driver.find_element(By.XPATH, Order.postal_xpath).send_keys(data.zip)
    driver.implicitly_wait(3)

    driver.find_element(By.XPATH, Order.continue_button).click()
    driver.implicitly_wait(3)

    # checkout step 2
    driver.find_element(By.XPATH, Order.finish_button).click()
    driver.implicitly_wait(2)

    assert driver.find_element(By.XPATH, Order.complete_header_xpath).text == data.complete_header
