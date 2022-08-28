from .Pages.locators import MainPageLocators, CatalogPageLocators, ProductPageLocators, AdminPageLocators, RegisterPageLocators
from .Pages.common_methods import CommonMethods

import pytest


@pytest.mark.main_page
@pytest.mark.parametrize('locator',
                         [MainPageLocators.SEARCH_FIELD,
                          MainPageLocators.NAV_BAR,
                          MainPageLocators.LOGO_FIELD,
                          MainPageLocators.PROFILE_BUTTON,
                          MainPageLocators.BASKET_BUTTON]
                         )
def test_main_page(driver, locator):
    main_page = CommonMethods(driver)
    assert main_page.check_element(*locator), f'Element not found {locator[1]}'


@pytest.mark.catalog_page
@pytest.mark.parametrize('locator',
                         [CatalogPageLocators.LEFT_NAVBAR,
                          CatalogPageLocators.PRODUCT_CARD,
                          CatalogPageLocators.BASKET_BTN_CARD,
                          CatalogPageLocators.LIKE_BTN_CARD,
                          CatalogPageLocators.SORT_BTN]
                         )
def test_catalog_page(driver, locator):
    catalog_page = CommonMethods(driver)
    assert catalog_page.check_element(*locator), f'Element not found {locator[1]}'


@pytest.mark.product_page
@pytest.mark.parametrize('locator',
                         [ProductPageLocators.PRODUCT_PHOTO,
                          ProductPageLocators.PRODUCT_PRICE,
                          ProductPageLocators.ADD_BTN,
                          ProductPageLocators.PRODUCT_NAME,
                          ProductPageLocators.LIKE_PRODUCT_BTN]
                         )
def test_catalog_page(driver, locator):
    catalog_page = CommonMethods(driver)
    assert catalog_page.check_element(*locator), f'Element not found {locator[1]}'


@pytest.mark.admin_page
@pytest.mark.parametrize('locator',
                         [AdminPageLocators.ADMIN_TITLE,
                          AdminPageLocators.USER_FIELD,
                          AdminPageLocators.PASSWORD_FIELD,
                          AdminPageLocators.FORGOTTEN_BTN,
                          AdminPageLocators.LOGIN_BTN]
                         )
def test_catalog_page(driver, locator):
    catalog_page = CommonMethods(driver)
    assert catalog_page.check_element(*locator), f'Element not found {locator[1]}'


@pytest.mark.register_page
@pytest.mark.parametrize('locator',
                         [RegisterPageLocators.FIRST_NAME_FIELD,
                          RegisterPageLocators.LAST_NAME_FIELD,
                          RegisterPageLocators.EMAIL_FIELD,
                          RegisterPageLocators.TELEPHONE_FIELD,
                          RegisterPageLocators.CONTINUE_BTN]
                         )
def test_catalog_page(driver, locator):
    catalog_page = CommonMethods(driver)
    assert catalog_page.check_element(*locator), f'Element not found {locator[1]}'




