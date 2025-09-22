import allure

from pages.admin_panel_page import AdminPanel


@allure.feature("Админ Панель")
class TestAdminPanel:
    @allure.title("Доступ к админ панели для пользователя с правами user")
    def test_user_role_not_permission(self, login_user, browser):
        page = AdminPanel(browser)
        page.open_admin_panel()
        page.check_permission_message()
