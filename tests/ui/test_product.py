import allure

from pages.product_pages import ProductPage


@allure.feature("Продукты")
class TestProducts:
    @allure.title("Добавить товар в корзину со страницы товара")
    def test_add_product_to_cart(self, browser, login_user):
        page = ProductPage(browser)
        page.open_product_page()
        page.select_product(2)
        product_name = page.get_product_name()
        page.click_add_cart_button()
        page.navbar.click_cart()
        page.check_products_in_cart(product_name)
