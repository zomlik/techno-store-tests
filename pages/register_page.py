import allure

from locators.register_locators_page import RegisterLocatorsPage
from pages.base_page import Basepage
from utils.url import Url


class RegisterPage(Basepage):
    locator = RegisterLocatorsPage()

    @allure.step("Открытие страницы регистрации")
    def open_register_page(self):
        self.open(Url.REGISTER)

    @allure.step("Заполнение формы регистрации")
    def fill_register_form(self,
                           first_name: str,
                           last_name: str,
                           email: str,
                           password: str) -> None:
        self.find_visible_el(self.locator.FIRST_NAME_FIELD).send_keys(first_name)
        self.find_visible_el(self.locator.LAST_NAME_FIELD).send_keys(last_name)
        self.find_visible_el(self.locator.EMAIL_FIELD).send_keys(email)
        self.find_visible_el(self.locator.PASSWORD_FIELD).send_keys(password)

    @allure.step("Клик на кнопку 'Регистрация'")
    def click_register_button(self) -> None:
        self.click_el(self.locator.REGISTER_BUTTON)
