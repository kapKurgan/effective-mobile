from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page

from utils.checks import check_attr, check_text, check_url

BASE_URL = 'https://www.saucedemo.com/'
PATH_PRODUCTS = 'inventory.html'
LOGO_PAGE_HOME = 'Swag Labs'
LOGO_INPUT_USERNAME = 'Username'
LOGO_INPUT_PASSWORD = 'Password'
LOGO_BUTTON_LOGIN = 'Login'
LOGO_PAGE_PRODUCTS = 'Products'


class PageLogin:
    def __init__(self, page: Page):
        self.page = page
        self.input_user_name = page.locator('#user-name')
        self.input_password = page.locator('#password')
        self.button_login = page.locator('#login-button')
        self.logo_url = page.locator('#root > div > div.login_logo')
        self.logo_product = page.locator('#header_container > div.header_secondary_container > span')

    def login(self, user_name: str, password: str):
        """
            Выполняет вход с заданными учетными данными.
        """
        check_attr(self.input_user_name, LOGO_INPUT_USERNAME, self.page, "placeholder")
        check_attr(self.input_password, LOGO_INPUT_PASSWORD, self.page, "placeholder")
        check_attr(self.button_login, LOGO_BUTTON_LOGIN, self.page, "value")

        self.input_user_name.fill(user_name)
        self.input_password.fill(password)

    def products(self):
        check_url(self.page, BASE_URL + PATH_PRODUCTS)
        check_text(self.logo_product, LOGO_PAGE_PRODUCTS, self.page)
