from selenium.webdriver.common.by import By


class RegisterLocatorsPage:
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "#firstname")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "#lastname")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")

    REGISTER_BUTTON = (By.CSS_SELECTOR, ".save")
