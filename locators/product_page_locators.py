from selenium.webdriver.common.by import By


class ProductPageLocators:
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".title")

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".cart")
