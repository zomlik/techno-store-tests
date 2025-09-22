import allure

from pages.cart_page import CartPage
from utils.url import Url


class TestCart:

    @allure.title("Переход на главную страницу по кнопке 'На главную'")
    def test_main_page_button(self, browser, login_user):
        page = CartPage(browser)
        page.open_cart_page()
        page.click_main_page_button()
        page.check_current_url(Url.PRODUCT)
