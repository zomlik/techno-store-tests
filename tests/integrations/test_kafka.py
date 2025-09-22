import allure
import pytest

from api.kafka_client import KafkaClient

@pytest.mark.skip
@allure.title("Отправка данных продуктов в Kafka")
def test_send_message_kafka(load_store_topic, result_store_topic, unique_group_id):
    product_data = [
        {"title": "Процессор 123", "price": "215", "categoryName": "CPU", "quantity": "98"}
    ]

    kafka_client = KafkaClient()
    kafka_client.produce_json_message(
        load_store_topic, product_data
    )
    received_messages = kafka_client.consume_json_messages(
        load_store_topic, unique_group_id, expected_count=2
    )

    print(received_messages)
