import allure
from httpx import Response

from api.api_client import ApiClient, api_client
from utils.url import Edpoints


class ProductClient(ApiClient):
    @allure.step("Загрузка продуктов из внешнего источника")
    def fetch_products(self) -> Response:
        return self.get(url=Edpoints.PRODUCTS)


def product_client() -> ProductClient:
    return ProductClient(client=api_client())
