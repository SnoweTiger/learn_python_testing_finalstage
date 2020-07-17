from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import  BasketPage

import time
import pytest

#  E:\MyProg\environments\selenium_env\Scripts\activate.bat

@pytest.mark.login_fakeuser
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        email = str(time.time()) + "@fakemail.org"
        password = "pCxQuMuhM"
        login_page.register_new_user(email,password)
        login_page.should_be_authorized_user()
        time.sleep(3)

    def test_user_cant_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        # time.sleep(10)
        page.should_not_be_success_message()


    def test_user_can_add_product_to_basket(self,browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser, link)
        page.open()
        page.push_add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_added_product_name()
        page.check_added_product_price()




def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    # time.sleep(3)

# @pytest.mark.parametrize('link',["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
# pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail(reason="some bug")),
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser):   #,link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.push_add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_added_product_name()
    page.check_added_product_price()

@pytest.mark.xfail(reason='must fail')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.push_add_to_basket()
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

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    basket_page = page.open_basket_for_guest()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_empty_basket_for_guest()
    basket_page.check_empty_basket_message()
