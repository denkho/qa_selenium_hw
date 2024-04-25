import time
from lesson_03.pages.order_page import OrderPage
from lesson_03.src.urls import Urls


class TestOrder:
    url = Urls()

    def test_order_with_wrong_credentials(self, driver):
        page = OrderPage(driver, self.url.base_url)
        page.open()
        page.login()
        page.order_with_wrong_credential()
        time.sleep(4)