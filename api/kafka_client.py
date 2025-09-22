import json
import time
from contextlib import contextmanager

import allure
from confluent_kafka import Consumer, KafkaError, Producer

from conf import settings


class KafkaClient:
    def __init__(self):
        self.bootstrap_servers = settings.kafka.bootstrap_servers

    @contextmanager
    def get_producer(self):
        producer = Producer({
            "bootstrap.servers": self.bootstrap_servers,
            "acks": "all"
        })
        try:
            yield producer
        finally:
            producer.flush()

    @contextmanager
    def get_consumer(self, group_id: str, topics: list[str]):
        consumer = Consumer({
            "bootstrap.servers": self.bootstrap_servers,
            "group.id": group_id,
            "auto.offset.reset": "earliest",
            "enable.auto.commit": False
        })
        consumer.subscribe(topics)
        try:
            yield consumer
        finally:
            consumer.close()

    @allure.step("Отправка сообщение в Kafka")
    def produce_json_message(self, topic: str, data: list[dict]) -> None:
        with self.get_producer() as producer:
            producer.produce(
                topic,
                value=json.dumps(data).encode('utf-8')
            )
            producer.poll(0)

    @allure.step("Получение сообщение из Kafka")
    def consume_json_messages(
            self,
            topic: str,
            group_id: str,
            expected_count: int = 1,
            timeout: float = 30.0
    ) -> list[dict]:
        messages = []
        start_time = time.time()

        with self.get_consumer(group_id, [topic]) as consumer:
            while len(messages) < expected_count and (time.time() - start_time) < timeout:
                msg = consumer.poll(1.0)

                if msg is None:
                    continue

                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        break
                    raise Exception(msg.error())

                try:
                    json_data = json.loads(msg.value().decode('utf-8'))
                    messages.append(json_data)
                except json.JSONDecodeError:
                    continue

        return messages
