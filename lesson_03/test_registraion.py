from selenium.webdriver.common.by import By
from data import Urls
from selenium.webdriver.support import expected_conditions as EC

def test_registration_explicit_waits(driver, wait):
    driver.get(Urls.url)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@id="startTest"]')))
    driver.find_element(By.XPATH, '//button[@id="startTest"]').click()

    driver.find_element(By.XPATH, '//input[@id="login"]').send_keys('login')
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('password')

    driver.find_element(By.XPATH, '//input[@id="agree"]').click()
    driver.find_element(By.XPATH, '//button[@id="register"]').click()

    wait.until(EC.visibility_of_element_located((By.XPATH, '//p[@id="successMessage"]')))

    assert driver.find_element(By.XPATH, '//p[@id="successMessage"]').text == 'Вы успешно зарегистрированы!'