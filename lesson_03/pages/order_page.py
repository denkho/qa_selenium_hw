from locators.main_locators import MainLocators
from locators.order_locators import OrderLocators
from locators.cart_locators import CartLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    order_locators = OrderLocators()
    main_locators = MainLocators()
    cart_locators = CartLocators()

    def order_with_wrong_credential(self):
        self.element_is_clickable(self.main_locators.SAUCE_LABS_BACKPACK).click()
        self.element_is_clickable(self.main_locators.CART_BTN).click()
        self.element_is_clickable(self.cart_locators.CHECKOUT_BTN).click()

