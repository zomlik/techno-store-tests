from locators.navbar_locators import NavBarLocators
from pages.base_page import Basepage


class NavBarComponents(Basepage):
    locator = NavBarLocators()

    def click_admin_panel(self):
        self.click_el(self.locator.ADMIN_PANEL_BUTTON)

    def click_cart(self):
        self.click_el(self.locator.CART_BUTTON)

    def click_exit(self):
        self.click_el(self.locator.EXIT_BUTTON)
