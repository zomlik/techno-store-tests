import allure
from httpx import Client, Response

from conf import settings


class ApiClient:
    def __init__(self, client: Client):
        self.client = client

    @allure.step("Отправка Get-запроса")
    def get(self, url: str) -> Response:
        return self.client.get(url)


def api_client() -> Client:
    return Client(
        base_url=settings.httpx.base_url,
        timeout=settings.httpx.timeout
    )
