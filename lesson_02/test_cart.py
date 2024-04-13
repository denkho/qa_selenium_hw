from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import data
from locators import Cart, Inventory, ItemCard, BurgerMenu


def test_add_item_to_cart_from_inventory(driver, authorize):
    item_name = driver.find_element(By.XPATH, Inventory.element_name).text
    item_name_for_cart_id = Cart.xpath_transformator_to_cart_button(item_name)
    driver.find_element(By.XPATH, item_name_for_cart_id).click()
    driver.implicitly_wait(2)

    driver.find_element(By.XPATH, Cart.cart_menu_icon).click()
    driver.implicitly_wait(2)
    assert driver.find_element(By.XPATH, Inventory.element_name).text == item_name

    # RESET app
    driver.find_element(By.XPATH, BurgerMenu.main_button).click()
    driver.implicitly_wait(2)
        
    driver.find_element(By.LINK_TEXT, BurgerMenu.reset_text).click()
    driver.implicitly_wait(2)


def test_delete_item_from_cart(driver, authorize):
    item_name = driver.find_element(By.XPATH, Inventory.element_name).text
    item_name_for_cart_id = Cart.xpath_transformator_to_cart_button(item_name)
    driver.find_element(By.XPATH, item_name_for_cart_id).click()
    driver.implicitly_wait(2)

    driver.find_element(By.XPATH, Cart.cart_menu_icon).click()
    driver.implicitly_wait(2)
    
    driver.get(data.url_cart)
    driver.find_element(By.XPATH, Cart.xpath_transformator_remove_from_cart_button(item_name)).click()
    
    try:
        driver.find_element(By.XPATH, Inventory.element_name)
    except NoSuchElementException:
        assert 0 == 0  

    # RESET app    
    driver.find_element(By.XPATH, BurgerMenu.main_button).click()
    driver.implicitly_wait(2)
        
    driver.find_element(By.LINK_TEXT, BurgerMenu.reset_text).click()
    driver.implicitly_wait(2)
    


def test_add_item_to_cart_from_item_card(driver, authorize):
    driver.find_element(By.XPATH, Inventory.element_name).click()
    item_name = driver.find_element(By.XPATH, Inventory.element_name).text
    driver.find_element(By.XPATH, ItemCard.add_to_cart_button).click()
    driver.get(data.url_cart)
    driver.implicitly_wait(2)
    assert item_name == driver.find_element(By.XPATH, Inventory.element_name).text

    # RESET app
    driver.find_element(By.XPATH, BurgerMenu.main_button).click()
    driver.implicitly_wait(2)
        
    driver.find_element(By.LINK_TEXT, BurgerMenu.reset_text).click()
    driver.implicitly_wait(2)


def test_delete_item_from_item_card(driver, authorize):
    driver.find_element(By.XPATH, Inventory.element_name).click()
    driver.find_element(By.XPATH, ItemCard.add_to_cart_button).click()
    driver.implicitly_wait(2)
    driver.find_element(By.XPATH, ItemCard.remove_button).click()

    driver.get(data.url_cart)
    driver.implicitly_wait(2)
    try:
        driver.find_element(By.XPATH, Inventory.element_name)
    except NoSuchElementException:
        assert 0 == 0  
    
    # RESET app
    driver.find_element(By.XPATH, BurgerMenu.main_button).click()
    driver.implicitly_wait(2)
        
    driver.find_element(By.LINK_TEXT, BurgerMenu.reset_text).click()
    driver.implicitly_wait(2)
    