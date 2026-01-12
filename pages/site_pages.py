from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page
from utils.checks import expect_visible, expect_text, expect_attr, expect_url

# page_login
BASE_URL = 'https://www.saucedemo.com/'
LOGO_PAGE_HOME = 'Swag Labs'
PLACEHOLDER_INPUT_USERNAME = 'Username'
PLACEHOLDER_INPUT_PASSWORD = 'Password'
VALUE_BUTTON_LOGIN = 'Login'

# page_products
PATH_PRODUCTS = 'inventory.html'
LOGO_PAGE_PRODUCTS = 'Products'


class SitePages:
    def __init__(self, page: Page):
        # page_login
        self.page = page
        self.input_user_name = page.locator('#user-name')
        self.input_password = page.locator('#password')
        self.button_login = page.locator('#login-button')
        self.logo_url = page.locator('#root > div > div.login_logo')
        self.error_text = page.locator('#login_button_container > div > form > div.error-message-container.error')

        # page_products
        self.logo_product = page.locator('#header_container > div.header_secondary_container > span')
        self.button_product_bm_open = page.locator('#react-burger-menu-btn')
        self.button_product_bm_close = page.locator('#react-burger-cross-btn')
        self.buttons_product_bm_list = page.locator('.bm-item-list >> a')


    def page_login(self, user_name: str, password: str):
        """
            Выполняет вход с заданными учетными данными.
        """
        expect_visible(self.input_user_name, PLACEHOLDER_INPUT_USERNAME)
        expect_attr(self.input_user_name, "placeholder", PLACEHOLDER_INPUT_USERNAME)
        self.input_user_name.fill(user_name)
        print(f"  ⌨️ В поле {PLACEHOLDER_INPUT_USERNAME} введено значение: {user_name}")

        expect_visible(self.input_password, PLACEHOLDER_INPUT_PASSWORD)
        expect_attr(self.input_password, "placeholder", PLACEHOLDER_INPUT_PASSWORD)
        self.input_password.fill(password)
        print(f"  ⌨️ В поле {PLACEHOLDER_INPUT_PASSWORD} введено значение: {password}")

        expect_visible(self.button_login, VALUE_BUTTON_LOGIN)
        expect_attr(self.button_login, "value", VALUE_BUTTON_LOGIN)


    def page_products(self):
        """
            Выполняет проверку перехода на страницу Products
        """
        expect_url(self.page, BASE_URL + PATH_PRODUCTS)
        expect_visible(self.logo_product, LOGO_PAGE_PRODUCTS)
        expect_text(self.logo_product, LOGO_PAGE_PRODUCTS)
