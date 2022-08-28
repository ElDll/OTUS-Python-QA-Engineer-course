from selenium.webdriver.common.by import By


class MainPageLocators:
    """locators for BasePage"""
    SEARCH_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Search"]')
    NAV_BAR = (By.CSS_SELECTOR, '.nav.navbar-nav')
    LOGO_FIELD = (By.CSS_SELECTOR, 'img[title="Your Store"]')
    PROFILE_BUTTON = (By.CSS_SELECTOR, '.fa.fa-user')
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn.btn-inverse.btn-block.btn-lg.dropdown-toggle')


class CatalogPageLocators:
    """locators for CatalogPage"""
    LEFT_NAVBAR = (By.CSS_SELECTOR, '#column-left')
    PRODUCT_CARD = (By.CSS_SELECTOR, '.product-thumb')
    BASKET_BTN_CARD = (
        By.CSS_SELECTOR,'div[class="product-layout product-grid col-lg-4 col-md-4 col-sm-6 col-xs-12"] button:nth-child(1)')
    LIKE_BTN_CARD = (
        By.CSS_SELECTOR, 'button[type="button"][data-toggle="tooltip"][data-original-title="Add to Wish List"]')
    SORT_BTN = (By.CSS_SELECTOR, '#input-sort')


class ProductPageLocators:
    """locators for ProductPage"""
    PRODUCT_PHOTO = (By.CSS_SELECTOR, 'ul[class="thumbnails"] li:nth-child(1) a:nth-child(1)')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'ul[class="list-unstyled"] li h2')
    ADD_BTN = (By.XPATH, '//button[@id="button-cart"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div[class="col-sm-4"] h1')
    LIKE_PRODUCT_BTN = (By.CSS_SELECTOR, 'div[id="product-product"] div[class="btn-group"] button:nth-child(1)')


class AdminPageLocators:
    """locators for AdminPage"""
    ADMIN_TITLE = (By.CSS_SELECTOR, '.panel-title')
    USER_FIELD = (By.CSS_SELECTOR, '#input-username')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#input-password')
    FORGOTTEN_BTN = (By.CSS_SELECTOR, 'a[href="http://192.168.1.76:8081/admin/index.php?route=common/forgotten"]')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[type="submit"]')


class RegisterPageLocators:
    """locators for RegisterPage"""
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '#input-firstname')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#input-email')
    TELEPHONE_FIELD = (By.CSS_SELECTOR, '#input-telephone')
    CONTINUE_BTN = (By.CSS_SELECTOR, 'input[value="Continue"]')
