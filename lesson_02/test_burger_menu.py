from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


import data
from locators import BurgerMenu, Inventory, Cart


def test_burger_menu_logout(driver, authorize):
    # logout test
    driver.find_element(By.XPATH, BurgerMenu.main_button).click()
    driver.implicitly_wait(2)
    driver.find_element(By.LINK_TEXT, BurgerMenu.logout_text).click()

    driver.implicitly_wait(2)

    assert driver.current_url == data.url


def test_burger_about_button(driver, authorize):
    # about button test
    driver.find_element(By.XPATH, BurgerMenu.main_button).click()
    driver.implicitly_wait(2)
    driver.find_element(By.LINK_TEXT, BurgerMenu.about_text).click()

    driver.implicitly_wait(2)

    assert driver.current_url == data.url_about


def test_burger_reset_app(driver, authorize):
    elements_in_inventory = driver.find_elements(By.XPATH, Inventory.element_name)
    elements_in_inventory = [element.text for element in elements_in_inventory]

    ids_to_cart_add = [Cart.xpath_transformator_to_cart_button(elem) for elem in elements_in_inventory]

    for one_id in ids_to_cart_add:
        driver.find_element(By.XPATH, one_id).click()
    
    driver.implicitly_wait(2)
    driver.get(data.url_cart)
    driver.implicitly_wait(2)

    # reset app test
    driver.find_element(By.XPATH, BurgerMenu.main_button).click()
    driver.implicitly_wait(2)
    
    driver.find_element(By.LINK_TEXT, BurgerMenu.reset_text).click()
    driver.implicitly_wait(2)
    
    try:
        driver.find_element(By.XPATH, Inventory.element_name)
    except NoSuchElementException:
        assert 0 == 0    
