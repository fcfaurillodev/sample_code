class InvalidParameters(Exception):
    """
    Invalid or incomplete parameter exception

    Expected parameter format did not matched or required parameters are missing
    """
    def __init__(self, details={}):
        super()
        self.code = 'SC4000'
        self.message = 'Invalid or incomplete parameters'
        self.details = details


class InvalidRequestHeaders(Exception):
    """
    Invalid request header exception

    Expected header format did not match or required headers are missing
    """
    def __init__(self, details={}):
        super()
        self.code = 'SC40005'
        self.message = 'Invalid request headers'
        self.details = details


class InvalidToken(Exception):
    """
    Invalid token exception

    Failed to authenticate token using the client keys
    """
    def __init__(self, details={}):
        super()
        self.code = 'SC40100'
        self.message = 'Failed to authenticate token'
        self.details = details


class MerchantNotFound(Exception):
    """
    Merchant not found exception

    Merchant ID is invalid or missing in the records
    """
    def __init__(self, details={}):
        super()
        self.code = 'SC40400'
        self.message = 'Merchant Not Found'
        self.details = details


class DuplicateMerchant(Exception):
    """
    Duplicate merchant exception

    Merchant with identity ID already exists
    """
    def __init__(self, details={}):
        super()
        self.code = 'SC40900'
        self.message = 'Duplicate Merchant'
        self.details = details