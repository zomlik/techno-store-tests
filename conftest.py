import pytest

from conf import LoginData, settings
from pages.login_page import LoginPage
from utils.url import Url


@pytest.fixture()
def user_data() -> LoginData:
    return settings.user


@pytest.fixture()
def admin_data() -> LoginData:
    return settings.admin


@pytest.fixture()
def login_user(browser, user_data):
    page = LoginPage(browser)
    page.open_login_page()
    page.fill_login_form(
        login=user_data.login,
        password=user_data.password
    )
    page.click_login_button()
    page.check_current_url(Url.PRODUCT)


@pytest.fixture()
def login_admin(browser, admin_data):
    page = LoginPage(browser)
    page.open_login_page()
    page.fill_login_form(
        login=admin_data.login,
        password=admin_data.password
    )
    page.click_login_button()
    page.check_current_url(Url.PRODUCT)
