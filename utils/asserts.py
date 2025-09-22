from typing import Any

import allure
from jsonschema import validate
from jsonschema.validators import Draft202012Validator


@allure.step("Проверка статус код равен {expected_code}")
def assert_status_code(actual_code: int, expected_code: int) -> None:
    assert actual_code == expected_code, f"Не верный статус код. exp:{expected_code}, act:{actual_code}"


@allure.step("Проверка соответствия JSON-схеме")
def validate_json_schema(instance: Any, schema: dict) -> None:
    validate(
        schema=schema,
        instance=instance,
        format_checker=Draft202012Validator
    )
