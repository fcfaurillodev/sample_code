import re
from jsonschema import Draft7Validator
from app.api.errors import InvalidParameters


class JSONSchema:
    """ A class to represent a JSON Schema """
    def __init__(self, schema):
        self._schema = schema
        self._validator = Draft7Validator(schema)

    def validate(self, value):
        """
        Accepts payload dict and validates if it complies with the json schema
        Returns
        -------
        :dict
            payload
        """
        raw_errors = self._validator.iter_errors(value)
        errors = self._format_errors(raw_errors)
        properties = self._schema['properties']
        if errors:
            result = {}
            for k, v in errors.items():
                result[k] = properties[k].get('message', v)
            raise InvalidParameters(result)
        return value

    def _format_errors(self, raw_errors):
        errors = {}
        for error in raw_errors:
            key = '.'.join(error.absolute_path)
            if key:
                errors[key] = error.message
            else:
                regex = r"'([a-zA-Z0-9_]+)' *"
                matched = re.match(regex, error.message)
                if matched:
                    errors[matched.group(1)] = error.message
                else:
                    return error.message
        return errors
