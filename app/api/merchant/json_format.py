from app.utils.json_schema import JSONSchema

__create_merchant = JSONSchema({
    'type': 'object',
    'properties': {
        'merchant_name': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 100,
            'message': 'Not a valid merchant name'
        },
        'description': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 255,
            'message': 'Not a valid description'
        },
        'contact_person': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 255,
            'message': 'Not a valid contact person'
        },
        'contact_number': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 100,
            'message': 'Not a valid pickup contact number'
        },
        'contact_email': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 255,
            'message': 'Not a valid email'
        },
        'address': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 255,
            'message': 'Not a valid address'
        },
        'identity_id': {
            'type': 'string',
            'maxLength': 100,
            'message': 'Not a valid identity id'
        }
    },
    'required': ['merchant_name', 'description', 'contact_person', 'contact_number', 'contact_email',
                 'address', 'identity_id']
})


__update_merchant = JSONSchema({
    'type': 'object',
    'properties': {
        'merchant_name': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 100,
            'message': 'Not a valid merchant name'
        },
        'description': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 255,
            'message': 'Not a valid description'
        },
        'contact_person': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 255,
            'message': 'Not a valid contact person'
        },
        'contact_number': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 100,
            'message': 'Not a valid pickup contact number'
        },
        'contact_email': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 255,
            'message': 'Not a valid email'
        },
        'address': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 255,
            'message': 'Not a valid address'
        }
    }
})