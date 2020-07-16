from .pages.product_page import ProductPage

import time
import pytest

@pytest.mark.xfail(reason='must fail')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.push_add_to_basket()
    page.should_not_be_success_message()
    time.sleep(3)

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    time.sleep(3)

@pytest.mark.xfail(reason='must fail')
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.push_add_to_basket()
    time.sleep(1)
    page.should_dissapear_success_message()
    time.sleep(3)
