from http import HTTPStatus

import allure

from api.product_client import product_client
from models.product_model import ListProductModel
from utils.asserts import assert_status_code, validate_json_schema


class TestProductApi:
    @allure.title("Загрузка продуктов из внешнего источника")
    def test_create_products(self):
        response = product_client().fetch_products()
        schema = ListProductModel.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(response.json(), schema.model_json_schema())
