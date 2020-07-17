from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert ("login" in self.browser.current_url),"URL does not contain login"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_MAIL),"Login form: mail input is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_PASS),"Login form: password input is not presented"

    def should_be_register_form(self):
         assert self.is_element_present(*LoginPageLocators.REG_FORM_MAIL),"Registration form: mail input is not presented"
         assert self.is_element_present(*LoginPageLocators.REG_FORM_PASS1),"Registration form: password input is not presented"
         assert self.is_element_present(*LoginPageLocators.REG_FORM_PASS2),"Registration form: confirm password input is not presented"

    def register_new_user(self, email, password):
        input_reg_form_mail = self.browser.find_element(*LoginPageLocators.REG_FORM_MAIL)
        input_reg_form_pass1 =  self.browser.find_element(*LoginPageLocators.REG_FORM_PASS1)
        input_reg_form_pass2 =  self.browser.find_element(*LoginPageLocators.REG_FORM_PASS2)
        reg_form_button =  self.browser.find_element(*LoginPageLocators.REG_FORM_BUTTON)
        input_reg_form_mail.send_keys(str(email))
        input_reg_form_pass1.send_keys(password)
        input_reg_form_pass2.send_keys(password)
        reg_form_button.click()
