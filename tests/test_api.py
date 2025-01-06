

def test_get_all_products(client, get_all_products_fixture):
    """
    Test the GET /products endpoint.
    Verifies:
    - Products are successfully fetched and validated.
    """
    get_all_products_fixture(client)


def test_get_single_product(client, validate_schema_fixture):
    """
    Test the GET /products/1 endpoint.
    Verifies:
    - Status code is 200.
    - Response matches the expected schema.
    """
    response = client.get("products/1")
    validate_schema_fixture(instance=response, schema_name="product_schema.json")


def test_create_and_validate_product(create_and_validate_product_fixture, client, test_data):
    """
    Test the end-to-end flow for creating and validating a new product.
    Verifies:
    - Product is successfully created.
    - Created product matches the input data.
    """
    create_and_validate_product_fixture(client, test_data)


def test_delete_product(client, delete_product_fixture):
    """
    Test the DELETE /products/<id> endpoint.
    Verifies:
    - Status code is 200.
    - Product is deleted successfully.
    """
    delete_product_fixture(client, product_id=1)
