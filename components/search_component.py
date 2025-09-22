import allure

from locators.search_locaotrs import SearchLocators
from pages.base_page import Basepage


class SearchComponent(Basepage):
    locator = SearchLocators()

    @allure.step("Заполнить поле поиска")
    def fill_search_field(self, value: str) -> None:
        self.find_visible_el(self.locator.SEARCH_FIELD).send_keys(value)

    @allure.step("Выбрать категорию {category}")
    def filter_by_cotegory(self, category: str) -> None:
        self.select_el(self.locator.CATEGORY_FILTER, category)

    @allure.step("Нажать на кнопку 'Поиск'")
    def click_find_button(self) -> None:
        self.click_el(self.locator.FIND_BUTTON)
