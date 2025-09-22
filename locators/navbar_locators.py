from selenium.webdriver.common.by import By


class NavBarLocators:
    ADMIN_PANEL_BUTTON = (By.XPATH, "//button[text()='Админ-панель']")
    CART_BUTTON = (By.XPATH, "//button[text()='Корзина']")
    EXIT_BUTTON = (By.XPATH, ".logout")
