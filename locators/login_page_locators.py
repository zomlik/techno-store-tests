from selenium.webdriver.common.by import By


class LoginPageLocator:
    LOGIN_FIELD = (By.CSS_SELECTOR, "#username")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".save")

    REGISTER_BUTTON = (By.CSS_SELECTOR, ".button")
