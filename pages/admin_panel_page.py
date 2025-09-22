import allure

from locators.admin_panel_locators import AdminPanelLocators
from pages.base_page import Basepage
from utils.url import Url


class AdminPanel(Basepage):
    locator = AdminPanelLocators

    @allure.step("Открытие Админ Панели")
    def open_admin_panel(self) -> None:
        self.open(Url.ADMIN_PANEL)

    @allure.step("Проверка сообщения об ошибке")
    def check_permission_message(self):
        el_text = self.find_visible_el(self.locator.PERMISSION_ERROR).text
        assert el_text == "У вас недостаточно прав для выполнения данного запроса"
