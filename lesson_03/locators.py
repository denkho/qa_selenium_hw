from selenium.webdriver.common.by import By


class Locators:
    button_start = (By.XPATH, '//button[@id="startTest"]')
    login_field = (By.XPATH, '//input[@id="login"]')
    password_field = (By.XPATH, '//input[@id="password"]')
    checkbox_agree = (By.XPATH, '//input[@id="agree"]')
    button_register = (By.XPATH, '//button[@id="register"]')

    message_success = (By.XPATH, '//p[@id="successMessage"]')