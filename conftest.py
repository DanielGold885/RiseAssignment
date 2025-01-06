import json
import os

import pytest

from business_flows.product_flows import create_and_validate_product
from business_flows.product_flows import create_new_product, validate_new_product_created
from configs.config import BASE_URL
from utils.api_client import ApiClient
from utils.schema_validator import validate_schema
from business_flows.product_flows import delete_product
from business_flows.product_flows import get_all_products_and_validate


@pytest.fixture
def base_url():
    """Fixture to provide the base URL."""
    return BASE_URL


@pytest.fixture
def client(base_url):
    """Fixture to initialize the API client."""
    return ApiClient(base_url)


@pytest.fixture(scope="session")
def test_data():
    """Fixture to load test data from JSON file."""
    config_path = os.path.join(os.path.dirname(__file__), "configs/test_data.json")
    with open(config_path, "r") as f:
        return json.load(f)


@pytest.fixture
def validate_schema_fixture():
    """
    Fixture to provide a callable function for schema validation.
    """
    return validate_schema


@pytest.fixture
def create_new_product_fixture():
    """
    Fixture to provide the create_new_product function.
    """
    return create_new_product


# @pytest.fixture
# def validate_new_product_created_fixture():
#     """
#     Fixture to provide the validate_new_product_created function.
#     """
#     return validate_new_product_created


@pytest.fixture
def create_and_validate_product_fixture():
    """
    Fixture to provide the high-level business flow for creating and validating a product.
    """
    return create_and_validate_product


@pytest.fixture
def delete_product_fixture():
    """
    Fixture to provide the delete_product function.
    """
    return delete_product


@pytest.fixture
def get_all_products_fixture():
    """
    Fixture to provide the get_all_products_and_validate function.
    """
    return get_all_products_and_validate
