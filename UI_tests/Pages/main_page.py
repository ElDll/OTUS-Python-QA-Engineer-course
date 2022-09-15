from selenium.common import TimeoutException
from UI_tests.Pages.common_methods import CommonMethods
from UI_tests.Pages.locators import MainPageLocators


class MainPage(CommonMethods):
    """В этом классе описаны методы для работы с главной страницей"""

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_register_page(self):
        self.click_element(*MainPageLocators.PROFILE_BUTTON)
        self.click_element(*MainPageLocators.REGISTER_BTN)

    def change_currency(self, currency):
        self.click_element(*MainPageLocators.SELECT_CURRENCY_BTN)
        if currency == 'dollar':
            self.click_element(*MainPageLocators.SELECT_DOLLAR)
        elif currency == 'euro':
            self.click_element(*MainPageLocators.SELECT_EURO)
        elif currency == 'pound':
            self.click_element(*MainPageLocators.SELECT_POUND)
        else:
            raise AssertionError('Передана неверная валюта')

    def check_currency_on_main_page(self, currency):
        basket_price = self.find_element(*MainPageLocators.BASKET_BUTTON_TEXT)
        if currency == 'dollar':
            try:
                self.find_element(MainPageLocators.PRODUCT_PRICE[0], MainPageLocators.PRODUCT_PRICE[1].format('$602.00'))
                if basket_price.text[-5] == '$':
                    return True
            except TimeoutException:
                return False
        elif currency == 'euro':
            try:
                self.find_element(MainPageLocators.PRODUCT_PRICE[0], MainPageLocators.PRODUCT_PRICE[1].format('472.33€'))
                if basket_price.text[-1] == '€':
                    return True
            except TimeoutException:
                return False
        elif currency == 'pound':
            try:
                self.find_element(MainPageLocators.PRODUCT_PRICE[0], MainPageLocators.PRODUCT_PRICE[1].format('£368.73'))
                if basket_price.text[-5] == '£':
                    return True
            except TimeoutException:
                return False
        else:
            raise AssertionError('Передана неверная валюта/Что-то пошло не так')

