from typing import Pattern

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from conf import settings


class Basepage:
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.wait = WebDriverWait(browser, settings.selenium.timeout)

    @allure.step("Открытие страницы")
    def open(self, url: str) -> None:
        return self.browser.get(url)

    @allure.step("Поиск элемента {locator}")
    def find_visible_el(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Поиск всех элементов {locator}")
    def finds_visible_els(self, locator: tuple[str, str]) -> list[WebElement]:
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Клик по элементу {locator}")
    def click_el(self, locator: tuple[str, str]) -> None:
        return self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Проверка текущего url")
    def check_current_url(self, expected_url: Pattern[str] | str) -> None:
        actual_url = self.browser.current_url
        assert actual_url == expected_url

    @allure.step("Выбрать элемент {value} из выпадающего списка")
    def select_el(self, locators: tuple[str, str], value: str) -> None:
        el = self.find_visible_el(locators)
        select = Select(el)
        select.select_by_value(value)
