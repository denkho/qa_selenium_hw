from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class BasePage():
    def __init__(self, driver: WebDriver, url) -> None:
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)

    
    def open(self):
        self.driver.get(self.url)

    
    def is_visible(self, locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))
    