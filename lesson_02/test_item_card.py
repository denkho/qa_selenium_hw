from selenium.webdriver.common.by import By

from locators import Inventory

def test_positive_go_to_item_card_page_from_inventory_item_image(driver, authorize):
    item_name = driver.find_element(By.XPATH, Inventory.element_name).text
    driver.find_element(By.XPATH, Inventory.create_img_xpath(item_name)).click()
    driver.implicitly_wait(3)

    assert driver.find_element(By.XPATH, Inventory.element_name).text == item_name


def test_positive_go_to_item_card_page_from_inventory_item_title(driver, authorize):
    item_name = driver.find_element(By.XPATH, Inventory.element_name).text
    driver.find_element(By.XPATH, Inventory.element_name).click()
    driver.implicitly_wait(3)

    assert driver.find_element(By.XPATH, Inventory.element_name).text == item_name
    