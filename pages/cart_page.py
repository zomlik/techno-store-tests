import allure

from components.navbar_component import NavBarComponents
from locators.cart_page_locators import CartPageLocators
from pages.base_page import Basepage
from utils.url import Url


class CartPage(Basepage):
    locator = CartPageLocators()

    def __init__(self, browser):
        super().__init__(browser)

        self.navbar = NavBarComponents(browser)

    @allure.step("Открытие страницы корзины")
    def open_cart_page(self) -> None:
        self.open(Url.CART)

    @allure.step("Клик на кнопку 'На главную'")
    def click_main_page_button(self) -> None:
        self.click_el(self.locator.GO_TO_MAIN_PAGE_BUTTON)
