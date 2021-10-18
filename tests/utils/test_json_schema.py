import pytest

from app.api import errors
from app.utils.json_schema import JSONSchema


def test_validate_with_valid_parameters():
    validator = JSONSchema({
        'type': 'object',
        'properties': {
            'key': {
                'type': 'string',
                'minLength': 1,
            },
        },
        'required': [
            'key'
        ]
    })

    stub_input = {'key': 'test'}
    assert validator.validate(stub_input) == stub_input


def test_validate_with_invalid_parameters():
    validator = JSONSchema({
        'type': 'object',
        'properties': {
            'key': {
                'type': 'string',
                'minLength': 1,
            },
        },
        'required': [
            'key'
        ]
    })

    with pytest.raises(errors.InvalidParameters):
        stub_input = {'key': None}
        validator.validate(stub_input)
