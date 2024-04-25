from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from src.user_data import UserData


class LoginPage(BasePage):
    locators = LoginLocators()
    user = UserData()


    def login(self):
        self.driver.find_element(*self.locators.USER_NAME).send_keys(self.user.STANDATD_USER)
        self.driver.find_element(*self.locators.PASSWORD).send_keys(self.user.PASSWORD)
        self.driver.find_element(*self.locators.LOGIN_BUTTON).click()
        