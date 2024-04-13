

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
    cart_menu_icon = ''


class Inventory:
    element_name = '//*[@data-test="inventory-item-name"]'
    add_to_cart_id = '//*[@data-test="add-to-cart-'