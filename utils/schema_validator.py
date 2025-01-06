import json
import os
from jsonschema import validate


def load_schema(schema_name):
    """
    Load a schema from the schemas folder.
    :param schema_name: Name of the schema file (e.g., product_schema.json).
    :return: The loaded schema as a dictionary.
    """
    schema_path = os.path.join(os.path.dirname(__file__), "../schemas", schema_name)
    with open(schema_path, "r") as schema_file:
        return json.load(schema_file)


def validate_schema(instance, schema_name):
    """
    Validate a JSON response against a schema.
    :param instance: The JSON response to validate.
    :param schema_name: Name of the schema file to validate against.
    :raises jsonschema.exceptions.ValidationError: If the validation fails.
    """
    schema = load_schema(schema_name)
    validate(instance=instance, schema=schema)
