from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group .btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items .row")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    #for login form
    LOGIN_FORM_MAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_FORM_PASS = (By.CSS_SELECTOR, "#id_login-password")
    #for registration form
    REG_FORM_MAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_FORM_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_FORM_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_FORM_BUTTON = (By.CSS_SELECTOR, '#register_form button[name="registration_submit"]')

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
