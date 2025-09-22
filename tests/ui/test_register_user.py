import allure

from pages.register_page import RegisterPage
from utils.fake_data import fake
from utils.url import Url


class TestRegisterUser:

    @allure.title("Регистрация пользователя с валидными данными")
    def test_create_new_user(self, browser):
        page = RegisterPage(browser)
        page.open_register_page()
        page.fill_register_form(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            password=fake.password()
        )
        page.click_register_button()
        page.check_current_url(Url.LOGIN)
