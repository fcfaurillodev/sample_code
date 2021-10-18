import uuid
import decimal

from app.utils import json_converter


def test_json_format_converter_with_uuid_object():
    stub_uuid = uuid.uuid4()
    converted_format = json_converter.json_format_converter(stub_uuid)

    assert isinstance(converted_format, str)
    assert converted_format == str(stub_uuid)


def test_json_format_converter_with_decimal_object():
    stub_decimal = decimal.Context(prec=5).create_decimal(1)
    converted_format = json_converter.json_format_converter(stub_decimal)

    assert isinstance(converted_format, float)
    assert converted_format == float(stub_decimal)
