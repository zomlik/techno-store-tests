import allure

from locators.login_page_locators import LoginPageLocator
from pages.base_page import Basepage
from utils.url import Url


class LoginPage(Basepage):
    locators = LoginPageLocator()

    @allure.step("Открытие страницы логин")
    def open_login_page(self) -> None:
        self.open(Url.LOGIN)

    @allure.step("Заполнение формы логина")
    def fill_login_form(self, login: str, password: str) -> None:
        self.find_visible_el(self.locators.LOGIN_FIELD).send_keys(login)
        self.find_visible_el(self.locators.PASSWORD_FIELD).send_keys(password)

    @allure.step("Клик на кнопку логин")
    def click_login_button(self) -> None:
        self.click_el(self.locators.LOGIN_BUTTON)

    @allure.step("Клик на кнопку регистрация")
    def click_register_button(self) -> None:
        self.click_el(self.locators.REGISTER_BUTTON)
