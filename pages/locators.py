from selenium.webdriver.common.by import By


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
