import allure
import pytest
from playwright.sync_api import Page
from pages.site_pages import BASE_URL, SitePages, LOGO_PAGE_HOME
from utils.checks import open_page, expect_url, expect_visible, expect_text


@allure.title("Подготовка тестового окружение (фикстура)")
@pytest.fixture
def open_home_page(page: Page) -> SitePages:
    """
        Открывает BASE_URL и жёстко проверяет совпадение адреса.
        При ЛЮБОЙ проблеме с навигацией тест ПАДАЕТ
    """
    print(f"\n⚙️ Подготовительные действия для теста")
    open_page(page, BASE_URL)
    expect_url(page, BASE_URL)
    login_page = SitePages(page)
    expect_visible(login_page.logo_url, LOGO_PAGE_HOME)
    expect_text(login_page.logo_url, LOGO_PAGE_HOME)
    return login_page