# pytest --headed --slowmo 1000 -s -v
# pytest --headed --slowmo 1000 -s -v --html=reports/pytest_report.html --capture=tee-sys --self-contained-html
# pytest --headed --slowmo 1000 -s -v --alluredir=reports/allure-results --capture=tee-sys
# allure serve reports/allure-results


import allure
import pytest

from utils.read_data import read_test_data_json

data_login_ok = read_test_data_json("data_tests/data_login_ok.json")


@allure.feature("Техническое задание: AQA Python")
@allure.story("Проверка разных сценариев авторизации")
@allure.title("Успешный логин")
@pytest.mark.parametrize("input_value", data_login_ok)
def test_login(open_main_page, input_value: str) -> None:
    # open_main_page уже на нужной странице
    login_page = open_main_page
    # Ввести данные
    login_page.login(input_value[0], input_value[1])
    login_page.button_login.click()


    login_page.products()
