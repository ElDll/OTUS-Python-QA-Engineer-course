from selenium.common import TimeoutException
from UI_tests.Pages.common_methods import CommonMethods
from UI_tests.Pages.locators import RegisterPageLocators
from ..data.register_page_data import first_name, last_name, email, telephone, password


class RegisterPage(CommonMethods):
    """В этом классе описаны методы для работы с главной страницей"""

    def __init__(self, driver):
        super().__init__(driver)

    def register_user(self):
        self.input_value(*RegisterPageLocators.FIRST_NAME_FIELD, first_name)
        self.input_value(*RegisterPageLocators.LAST_NAME_FIELD, last_name)
        self.input_value(*RegisterPageLocators.EMAIL_FIELD, email)
        self.input_value(*RegisterPageLocators.TELEPHONE_FIELD, telephone)
        self.input_value(*RegisterPageLocators.PASSWORD_FIELD, password)
        self.input_value(*RegisterPageLocators.CONFIRM_PASSWORD_FIELD, password)
        self.click_element(*RegisterPageLocators.PRIVACY_POLICY_CHECKBOX)
        self.click_element(*RegisterPageLocators.CONTINUE_BTN)

    def check_created_header(self):
        try:
            self.find_element(*RegisterPageLocators.CREATED_HEADER)
            return True
        except TimeoutException:
            return False
