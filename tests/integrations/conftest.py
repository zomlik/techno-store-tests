import time

import pytest


@pytest.fixture()
def load_store_topic():
    return "out_store.shop_store.products_info"


@pytest.fixture()
def result_store_topic():
    return "shop_store.out_store.products_info"


@pytest.fixture()
def unique_group_id():
    return f"test-group-{int(time.time())}-{time.perf_counter_ns()}"
