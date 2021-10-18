import decimal
import uuid

def json_format_converter(obj):
    """ Converts obj of uuid and decimal type to json serializable value"""
    if isinstance(obj, uuid.UUID):
        return str(obj)
    elif isinstance(obj, decimal.Decimal):
        return float(obj)
    else:
        return obj