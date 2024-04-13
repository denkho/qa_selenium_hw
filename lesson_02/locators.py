

class MainPage:
    username_field = '//*[@id="user-name"]'
    password_field = '//*[@id="password"]'
    login_button = '//*[@id="login-button"]'
    login_error_message = '//*[@data-test="error"]'
    login_error_message_text = 'Epic sadface: Username and password do not match any user in this service'


class BurgerMenu:
    main_button = '//button[@id="react-burger-menu-btn"]'
    logout_text = 'Logout'
    about_text = 'About'
    reset_text = 'Reset App State'
    

class Cart:
    cart_menu_icon = '//*[@data-test="shopping-cart-link"]'

    @staticmethod
    def xpath_transformator_to_cart_button(item_name):
        item_name_prepared = '-'.join(item_name.lower().split())
        item_name_for_cart_id = Inventory.add_to_cart_id + item_name_prepared + '"]'
        return item_name_for_cart_id

    @staticmethod
    def xpath_transformator_remove_from_cart_button(item_name):
        item_name_prepared = '-'.join(item_name.lower().split())
        item_name_for_cart_id = Inventory.remove_from_cart_id + item_name_prepared + '"]'
        return item_name_for_cart_id


class Inventory:
    element_name = '//*[@data-test="inventory-item-name"]'
    item_price = '//*[@data-test="inventory-item-price"]'
    add_to_cart_id = '//*[@data-test="add-to-cart-'
    remove_from_cart_id = '//*[@data-test="remove-'

class InventoryFilter:
    sort_container = '//*[@data-test="product-sort-container"]'
    sort_ZA_id = '//option[@value="za"]'
    sort_AZ_id = '//option[@value="az"]'
    sort_HiLo_id = '//option[@value="hilo"]'
    sort_LoHi_id = '//option[@value="lohi"]'

class ItemCard:
    add_to_cart_button = '//button[@data-test="add-to-cart"]'
    remove_button = '//button[@data-test="remove"]'