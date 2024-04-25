import time
from pages.login_page import LoginPage
from src.urls import Urls
from locators.main_locators import MainLocators

class TestLogin:
    url = Urls()
    main_locators = MainLocators()
    
    def test_login(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        page.login()
        expected = 'Products'
        actual_text = page.get_text(self.main_locators.TITLE)
        assert actual_text == expected, f'Unexpected text, expected {expected}, actual {actual_text}'
        time.sleep(1)


    def test_login1(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        page.login()
        
        cards = page.get_length(self.main_locators.CARDS)
        expected_len = 6
        assert cards == expected_len, f"Expected: {expected_len}, actual {len(cards)}"
