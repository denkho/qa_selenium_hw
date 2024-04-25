from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from lesson_03.locators.login_locators import LoginLocators
from lesson_03.src.user_data import UserData

 
class BasePage:

    timeout = 10

    locators = LoginLocators()
    user = UserData()

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def login(self):
        self.element_is_visible(self.locators.USER_NAME).send_keys(self.user.STANDATD_USER)
        self.element_is_visible(self.locators.PASSWORD).send_keys(self.user.PASSWORD)
        self.element_is_clickable(self.locators.LOGIN_BUTTON).click()


    def open(self):
        self.driver.get(self.url)


    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def get_length(self, locator):
        return len(self.driver.find_elements(*locator))

    def click_to_element(self, locator):
        self.driver.find_element(*locator).click()

    def element_is_clickable(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    
    def element_is_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))