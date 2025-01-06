from jsonschema import validate
from jsonschema.exceptions import ValidationError


def create_new_product(client, product_data):
    """
    Business flow to create a new product.
    :param client: API client instance.
    :param product_data: Dictionary containing product details.
    :return: The response JSON for the created product.
    :raises AssertionError: If the product creation fails.
    """
    response = client.post("products", data=product_data)
    if "id" not in response:
        raise AssertionError("Product creation failed, no ID returned.")
    return response


def validate_new_product_created(product_response, expected_product_data):
    """
    Validate that the newly created product matches the expected data.
    :param product_response: The response JSON of the created product.
    :param expected_product_data: The original data used to create the product.
    :raises AssertionError: If validation fails.
    """
    for key in expected_product_data:
        assert product_response.get(key) == expected_product_data[key], \
            f"Mismatch for field '{key}': expected {expected_product_data[key]}, got {product_response.get(key)}"


def create_and_validate_product(client, test_data):
    """
    High-level business flow to create and validate a new product.
    :param client: API client instance.
    :param test_data: Full test data dictionary containing 'new_product'.
    """
    # Step 1: Extract product data
    new_product_data = test_data["new_product"]

    # Step 2: Create a new product
    created_product = create_new_product(client, new_product_data)

    # Step 3: Validate the created product
    validate_new_product_created(created_product, new_product_data)


def delete_product(client, product_id):
    """
    Business flow to delete a product.
    :param client: API client instance.
    :param product_id: ID of the product to delete.
    :raises AssertionError: If the deletion fails.
    """
    response_code = client.delete(f"products/{product_id}")
    if response_code != 200:
        raise AssertionError(f"Failed to delete product with ID {product_id}. "
                             f"Expected status code 200, got {response_code}")
    print(f"Product with ID {product_id} deleted successfully.")


def get_all_products_and_validate(client):
    """
    Business flow to fetch all products and validate the response.
    :param client: API client instance.
    :return: List of products.
    :raises AssertionError: If the response is not a valid list or is empty.
    """
    response = client.get("products")
    if not isinstance(response, list):
        raise AssertionError(f"Expected response to be a list, got {type(response)}.")
    if len(response) == 0:
        raise AssertionError("No products found in the response.")
    print(f"Fetched {len(response)} products successfully.")
    return response
