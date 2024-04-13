from selenium.webdriver.common.by import By

from locators import Inventory, InventoryFilter


def test_filter_A_Z(driver, authorize):
    # sort inversed order 
    driver.find_element(By.XPATH, InventoryFilter.sort_container).click()
    driver.find_element(By.XPATH, InventoryFilter.sort_ZA_id).click()
    driver.implicitly_wait(2)
    
    # sort AZ to check 
    driver.find_element(By.XPATH, InventoryFilter.sort_container).click()
    driver.find_element(By.XPATH, InventoryFilter.sort_AZ_id).click()
    driver.implicitly_wait(2)

    # get list of names of all items
    elements = driver.find_elements(By.XPATH, Inventory.element_name)
    elements = [element.text for element in elements]
    elements_ordered = sorted(elements)

    assert elements == elements_ordered


def test_filter_Z_A(driver, authorize):
    # sort inversed order 
    driver.find_element(By.XPATH, InventoryFilter.sort_container).click()
    driver.find_element(By.XPATH, InventoryFilter.sort_AZ_id).click()
    driver.implicitly_wait(2)
    
    # sort AZ to check 
    driver.find_element(By.XPATH, InventoryFilter.sort_container).click()
    driver.find_element(By.XPATH, InventoryFilter.sort_ZA_id).click()
    driver.implicitly_wait(2)

    # get list of names of all items
    elements = driver.find_elements(By.XPATH, Inventory.element_name)
    elements = [element.text for element in elements]
    elements_ordered = sorted(elements, reverse=True)

    assert elements == elements_ordered

    
def test_filter_Lo_High(driver, authorize):
    # sort inversed order 
    driver.find_element(By.XPATH, InventoryFilter.sort_container).click()
    driver.find_element(By.XPATH, InventoryFilter.sort_HiLo_id).click()
    driver.implicitly_wait(2)

    # sort Lo High to check 
    driver.find_element(By.XPATH, InventoryFilter.sort_container).click()
    driver.find_element(By.XPATH, InventoryFilter.sort_LoHi_id).click()
    driver.implicitly_wait(2)

    # get list of names of all items
    elements = driver.find_elements(By.XPATH, Inventory.item_price)
    elements = [float(element.text[1:]) for element in elements]
    elements_ordered = sorted(elements)

    assert elements == elements_ordered


def test_filter_High_Lo(driver, authorize):
    # sort inversed order 
    driver.find_element(By.XPATH, InventoryFilter.sort_container).click()
    driver.find_element(By.XPATH, InventoryFilter.sort_LoHi_id).click()
    driver.implicitly_wait(2)

    # sort High Lo to check 
    driver.find_element(By.XPATH, InventoryFilter.sort_container).click()
    driver.find_element(By.XPATH, InventoryFilter.sort_HiLo_id).click()
    driver.implicitly_wait(2)

    # get list of names of all items
    elements = driver.find_elements(By.XPATH, Inventory.item_price)
    elements = [float(element.text[1:]) for element in elements]
    elements_ordered = sorted(elements, reverse=True)

    assert elements == elements_ordered
