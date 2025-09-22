from enum import Enum

from conf import settings


class Url(str, Enum):
    BASE_PAGE = settings.selenium.base_url
    LOGIN = f"{BASE_PAGE}/login"
    REGISTER = f"{BASE_PAGE}/register"
    PRODUCT = f"{BASE_PAGE}/index"
    CART = f"{BASE_PAGE}/cart"
    ADMIN_PANEL = f"{BASE_PAGE}/admin"

    def __str__(self):
        return self.value


class Edpoints(str, Enum):
    PRODUCTS = "/products/fetch"

    def __str__(self):
        return self.value
