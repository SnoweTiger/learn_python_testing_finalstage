from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def check_empty_basket_message(self):
        basket_message = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE)
        basket_message_text = basket_message.text
        message_dict = {"ar": "سلة التسوق فارغة","ca": "La seva cistella està buida.",
        "cs": "Váš košík je prázdný.","da": "Din indkøbskurv er tom.",
        "de": "Ihr Warenkorb ist leer.","en": "Your basket is empty.",
        "el": "Το καλάθι σας είναι άδειο.","es": "Tu carrito esta vacío.",
        "fi": "Korisi on tyhjä","fr": "Votre panier est vide.","it": "Il tuo carrello è vuoto.",
        "ko": "장바구니가 비었습니다.","nl": "Je winkelmand is leeg",
        "pl": "Twój koszyk jest pusty.","pt": "O carrinho está vazio.",
        "pt-br": "Sua cesta está vazia.","ro": "Cosul tau este gol.",
        "ru": "Ваша корзина пуста","sk": "Váš košík je prázdny",
        "uk": "Ваш кошик пустий.","zh-cn": "Your basket is empty."}
        assert (message_dict['en'] in basket_message_text ),'Basket is not empty'

    def check_empty_basket_for_guest(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET),\
        "Success message is presented, but should not be"
