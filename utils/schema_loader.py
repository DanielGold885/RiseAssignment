import json
import os


def load_schema(schema_name):
    """
    Load a schema from the schemas folder.
    :param schema_name: Name of the schema file (e.g., product_schema.json).
    :return: The loaded schema as a dictionary.
    """
    schema_path = os.path.join(os.path.dirname(__file__), f"../schemas/{schema_name}")
    with open(schema_path, "r") as schema_file:
        return json.load(schema_file)
