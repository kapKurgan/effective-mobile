import allure
import pytest
from playwright.sync_api import Page
from pages.site_pages import BASE_URL, SitePages, LOGO_PAGE_HOME
from utils.checks import open_page, check_url, check_text, check_locator


@allure.title("Подготовка тестового окружение (фикстура)")
@pytest.fixture
def open_home_page(page: Page) -> SitePages:
    """
        Открывает BASE_URL и жёстко проверяет совпадение адреса.
        При ЛЮБОЙ проблеме с навигацией тест ПАДАЕТ
    """
    print(f"\n⚙️ Подготовительные действия для теста")
    open_page(page, BASE_URL)
    check_url(page, BASE_URL)
    login_page = SitePages(page)
    check_locator(login_page.logo_url, LOGO_PAGE_HOME, page)
    check_text(login_page.logo_url, LOGO_PAGE_HOME, page)
    return login_page