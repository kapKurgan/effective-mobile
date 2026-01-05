import allure
import pytest
from playwright.sync_api import Page
from locators.page_login import BASE_URL, PageLogin, LOGO_PAGE_HOME
from utils.checks import open_page, check_url, check_text


@allure.title("Подготовка тестового окружение (фикстура)")
@pytest.fixture
def open_main_page(page: Page) -> PageLogin:
    """
        Открывает BASE_URL и жёстко проверяет совпадение адреса.
        При ЛЮБОЙ проблеме с навигацией тест ПАДАЕТ
    """
    open_page(page, BASE_URL)
    check_url(page, BASE_URL)
    login_page = PageLogin(page)
    check_text(login_page.logo_url, LOGO_PAGE_HOME, page)
    return login_page