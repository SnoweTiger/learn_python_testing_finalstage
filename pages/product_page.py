from .base_page import BasePage
from .locators import ProductPageLocators

from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def push_add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_added_product_name(self):
        added_product = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME)
        added_product_name = added_product.text
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name = product.text
        print('Selected: ',product_name,' Added: ', added_product_name)
        assert (product_name == added_product_name),'Added another product'

    def check_added_product_price(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        basket_price_text = basket_price.text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_text = product_price.text
        print('Selected price:',product_price_text,' Added price:', basket_price_text)
        assert (product_price_text == basket_price_text),'Added with another price'
