from selenium.webdriver.common.by import By


class SearchLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, "#search")
    CATEGORY_FILTER = (By.CSS_SELECTOR, "#category")

    FIND_BUTTON = (By.CSS_SELECTOR, "//input[@value='Поиск!']")
