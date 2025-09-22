import allure

from components.navbar_component import NavBarComponents
from locators.product_page_locators import ProductPageLocators
from pages.base_page import Basepage
from utils.url import Url


class ProductPage(Basepage):
    locator = ProductPageLocators()

    def __init__(self, browser):
        super().__init__(browser)

        self.navbar = NavBarComponents(browser)

    @allure.step("Открытие страницы с продуктами")
    def open_product_page(self) -> None:
        self.open(Url.PRODUCT)

    @allure.step("Переход на страницу выбранного продукта")
    def select_product(self, product: int = 0) -> None:
        els = self.finds_visible_els(self.locator.PRODUCT_TITLE)[product]
        els.click()

    @allure.step("Нажать на кнопку 'В корзину'")
    def click_add_cart_button(self) -> None:
        self.click_el(self.locator.ADD_TO_CART_BUTTON)

    @allure.step("Проверка, что товар находится в корзине")
    def check_products_in_cart(self, value: str, product_num: int = 0) -> None:
        text_el = self.finds_visible_els(self.locator.PRODUCT_TITLE)[product_num].text
        assert text_el == value, f"Товар {value} отсутствует в корзине"

    @allure.step("Получить наименование продукта")
    def get_product_name(self, product_num: int = 0) -> str:
        els = self.finds_visible_els(self.locator.PRODUCT_TITLE)[product_num]
        return els.text
