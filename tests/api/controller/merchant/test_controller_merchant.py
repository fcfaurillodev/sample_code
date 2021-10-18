import pytest
from faker import Faker
from faker.generator import random
from uuid import uuid4
import time


from app.api.merchant import controller
from app.store.merchant import store
from app.store.merchant.model.merchant import Merchant
from app.api import errors
from app.config import Config


@pytest.fixture(scope='session')
def app(request):
    from app import create_app
    return create_app('testing')


@pytest.fixture(autouse=True)
def app_context(app):
    """Creates a flask app context"""
    with app.app_context():
        yield app


@pytest.fixture
def request_context(app_context):
    """Creates a flask request context"""
    return app_context.test_request_context()


@pytest.fixture
def client(app_context):
    return app_context.test_client(use_cookies=True)


@pytest.fixture
def fake_merchant():
    fake = Faker()
    return {
        'id': 1,
        'merchant_name': fake.name(),
        'identity_id': str(uuid4()),
        'description': fake.sentence(),
        'contact_person': fake.name(),
        'contact_number': fake.msisdn(),
        'contact_email': fake.email(),
        'address': fake.sentence(),
        'created_at': time.time(),
        'updated_at': time.time()
    }

@pytest.fixture
def fake_merchant_obj() -> Merchant:
    return Merchant.from_dict(fake_merchant.__dict__)


@pytest.fixture
def fake_merchant_list() -> Merchant:
    return [fake_merchant, fake_merchant]

@pytest.fixture
def fake_new_merchant_details():
    fake = Faker()
    return {
        'id': 1,
        'merchant_name': fake.name(),
        'identity_id': str(uuid4()),
        'description': fake.sentence(),
        'contact_person': fake.name(),
        'contact_number': fake.msisdn(),
        'contact_email': fake.email(),
        'address': "New Address",
        'created_at': time.time(),
        'updated_at': time.time()
    }


@pytest.mark.parametrize("merchant_id", [(2), (10), (100)])
def test_get_merchant_with_invalid_merchant_id(mocker, client, fake_merchant, merchant_id):
    """ Should raise Merchant Not Found error for invalid merchant id in get_merchant """
    with client as c:
        with pytest.raises(errors.MerchantNotFound):
            mocked_get_merchant = mocker.patch.object(store, 'get_merchant', return_value=None)
            controller.get_merchant(merchant_id)
            mocked_get_merchant.assert_called_with(merchant_id)


@pytest.mark.parametrize("merchant_id", [(1)])
def test_get_merchant_with_valid_merchant_id(mocker, client, fake_merchant_obj, merchant_id):
    """ Should return Merchant Object for valid merchant id in get_merchant """
    with client as c:
        mocked_get_merchant = mocker.patch.object(store, 'get_merchant', return_value=fake_merchant_obj)
        result = controller.get_merchant(merchant_id)
        mocked_get_merchant.assert_called_once()
        mocked_get_merchant.assert_called_with(merchant_id=merchant_id)
        assert result == fake_merchant_obj.to_dict()


@pytest.mark.parametrize("page, limit", [('a', '10'), ('0', '10')])
def test_get_merchants_with_invalid_page_arg(mocker, request_context, page, limit):
    """ Should raise Invalid Parameter error for invalid type and value of page request arg in get_merchants"""
    with request_context as r:
        r.request.args = {"page": page, "limit": limit}
        with pytest.raises(errors.InvalidParameters):
            mocked_get_merchants = mocker.patch.object(store, 'get_merchants', return_value=None)
            controller.get_merchants()
            mocked_get_merchant.assert_not_called()


@pytest.mark.parametrize("page, limit", [('1', '0'), ('1', 'a')])
def test_get_merchants_with_invalid_limit_arg(mocker, request_context, page, limit):
    """ Should raise Invalid Parameter error for invalid type and value of limit request arg in get_merchants"""
    with request_context as r:
        r.request.args = {"page": page, "limit": limit}
        with pytest.raises(errors.InvalidParameters):
            mocked_get_merchants = mocker.patch.object(store, 'get_merchants', return_value=None)
            controller.get_merchants()
            mocked_get_merchants.assert_not_called()


@pytest.mark.parametrize("page, limit", [('1', '10'), ('1', '100')])
def test_get_merchants_with_valid_args(mocker, request_context, page, limit):
    """ Should return list of merchants with page and limit set in request param in get_merchants"""
    with request_context as r:
        r.request.args = {"page": page, "limit": limit}
        mocked_get_merchants = mocker.patch.object(store, 'get_merchants', return_value=fake_merchant_list)
        res_merchants, res_page, res_limit = controller.get_merchants()
        mocked_get_merchants.assert_called_once()
        mocked_get_merchants.assert_called_with(limit=int(limit), offset=0)
        assert res_merchants == fake_merchant_list
        assert res_page == page
        assert res_limit == limit


def test_get_merchants_with_no_args(mocker, request_context):
    """ Should return list of merchants with default page and limit in get_merchants """
    with request_context as r:
        mocked_get_merchants = mocker.patch.object(store, 'get_merchants', return_value=fake_merchant_list)
        res_merchants, res_page, res_limit = controller.get_merchants()
        mocked_get_merchants.assert_called_once()
        mocked_get_merchants.assert_called_with(limit=int(Config.DEFAULT_PAGINATION_LIMIT), offset=0)
        assert res_merchants == fake_merchant_list
        assert res_page == '1'
        assert res_limit == Config.DEFAULT_PAGINATION_LIMIT


def test_create_merchant_with_valid_request_body(mocker, request_context, fake_merchant):
    """ Should return merchant dict for valid request params in create_merchant """
    with request_context as r:
        fake_merchant_obj = Merchant.from_dict(fake_merchant)
        mocked_get_merchant_by_identity = mocker.patch.object(store, 'get_merchant_by_identity', return_value=None)
        mocked_create_merchant = mocker.patch.object(store, 'create_merchant', return_value=fake_merchant_obj)
        result = controller.create_merchant(fake_merchant)
        mocked_get_merchant_by_identity.assert_called_once()
        mocked_get_merchant_by_identity.assert_called_with(identity_id=fake_merchant['identity_id'])
        mocked_create_merchant.assert_called_once()
#         mocked_create_merchant.assert_called_with(merchant=Merchant.from_dict(fake_merchant))
        assert result['id'] == 1
        assert result['identity_id'] == fake_merchant['identity_id']


def test_create_merchant_with_duplicate_identity_id(mocker, request_context, fake_merchant):
    """ Should raise Duplicate Merchant error for invalid identity_id param in create_merchant """
    with request_context as r:
        with pytest.raises(errors.DuplicateMerchant):
            fake_merchant_obj = Merchant.from_dict(fake_merchant)
            mocked_get_merchant_by_identity = mocker.patch.object(store, 'get_merchant_by_identity', return_value=fake_merchant_obj)
            mocked_create_merchant = mocker.patch.object(store, 'create_merchant', return_value=fake_merchant_obj)
            result = controller.create_merchant(fake_merchant)
            mocked_get_merchant_by_identity.assert_called_once()
            mocked_get_merchant_by_identity.assert_called_with(identity_id=fake_merchant['identity_id'])
            mocked_create_merchant.assert_not_called_once()


@pytest.mark.parametrize("body", [({"merchant_name": "Sample Merchant",
                                     "identity_id": 11111,
                                     "description": "sample description",
                                     "contact_number": "092000000",
                                     "contact_email": "sample@mail.com",
                                     "contact_person": "sample name",
                                     "address": "sample address"
                                   }),
                                   ({"merchant_name": "Sample Merchant",
                                      "identity_id": "123345",
                                      "description": "sample description",
                                      "contact_number": "092000000",
                                      "contact_email": "",
                                      "contact_person": "sample name",
                                      "address": "sample address"
                                    })])
def test_create_merchant_with_invalid_request_body(mocker, request_context, body):
    """ Should raise Invalid Parameter error for invalid param passed in create_merchant"""
    with request_context as r:
        with pytest.raises(errors.InvalidParameters):
            mocked_get_merchant_by_identity = mocker.patch.object(store, 'get_merchant_by_identity', return_value=None)
            mocked_create_merchant = mocker.patch.object(store, 'create_merchant', return_value=None)
            result = controller.create_merchant(body)
            mocked_get_merchant_by_identity.assert_not_called_once()
            mocked_create_merchant.assert_not_called_once()


@pytest.mark.parametrize("body", [({"merchant_name": "Sample Merchant",
                                     "identity_id": 11111,
                                     "description": "sample description",
                                     "contact_number": "092000000",
                                     "contact_email": "sample@mail.com",
                                     "contact_person": "sample name"
                                   }),
                                   ({"merchant_name": "Sample Merchant",
                                      "contact_person": "sample name",
                                      "address": "sample address"
                                    })])
def test_create_merchant_with_incomplete_request_body(mocker, request_context, body):
    """ Should raise Invalid Parameter error for incomplete param passed in create_merchant"""
    with request_context as r:
        with pytest.raises(errors.InvalidParameters):
            mocked_get_merchant_by_identity = mocker.patch.object(store, 'get_merchant_by_identity', return_value=None)
            mocked_create_merchant = mocker.patch.object(store, 'create_merchant', return_value=None)
            result = controller.create_merchant(body)
            mocked_get_merchant_by_identity.assert_not_called_once()
            mocked_create_merchant.assert_not_called_once()


@pytest.mark.parametrize("merchant_id, new_merchant_details", [(1, {"address": "New Address"})])
def test_update_merchant_with_valid_request_body(mocker, request_context, fake_new_merchant_details, merchant_id, new_merchant_details):
    """ Should return merchant dict for valid request params in update_merchant """
    with request_context as r:
        new_merchant_details_obj = Merchant.from_dict(new_merchant_details)
        fake_merchant_obj = Merchant.from_dict(fake_new_merchant_details)
        mocked_get_merchant = mocker.patch.object(store, 'get_merchant', return_value=fake_merchant_obj)
        mocked_update_merchant = mocker.patch.object(store, 'update_merchant', return_value=fake_merchant_obj)
        result = controller.update_merchant(merchant_id=merchant_id, body=new_merchant_details)
        mocked_get_merchant.assert_called_once()
        mocked_get_merchant.assert_called_with(merchant_id=merchant_id)
        mocked_update_merchant.assert_called_once()
#         mocked_update_merchant.assert_called_with(merchant_id=merchant_id,
#                                                   new_merchant_details=new_merchant_details_obj)
        assert result['address'] == new_merchant_details['address']


@pytest.mark.parametrize("merchant_id, new_merchant_details", [(1, {"address": ""})])
def test_update_merchant_with_invalid_request_body(mocker, request_context, fake_new_merchant_details, merchant_id, new_merchant_details):
    """ Should raise Invalid Parameters error for invalid address value in update_merchant """
    with request_context as r:
        with pytest.raises(errors.InvalidParameters):
            new_merchant_details_obj = Merchant.from_dict(new_merchant_details)
            fake_merchant_obj = Merchant.from_dict(fake_new_merchant_details)
            mocked_get_merchant = mocker.patch.object(store, 'get_merchant', return_value=fake_merchant_obj)
            mocked_update_merchant = mocker.patch.object(store, 'update_merchant', return_value=fake_merchant_obj)
            result = controller.update_merchant(merchant_id=merchant_id, body=new_merchant_details)
            mocked_get_merchant.assert_not_called_once()
            mocked_update_merchant.assert_not_called_once()

@pytest.mark.parametrize("merchant_id, new_merchant_details", [(1000, {"address": "test"})])
def test_update_merchant_with_nonexisting_merchant(mocker, request_context, fake_new_merchant_details, merchant_id, new_merchant_details):
    """ Should raise Merchant not Found error for invalid merchant id update_merchant """
    with request_context as r:
        with pytest.raises(errors.MerchantNotFound):
            new_merchant_details_obj = Merchant.from_dict(new_merchant_details)
            fake_merchant_obj = Merchant.from_dict(fake_new_merchant_details)
            mocked_get_merchant = mocker.patch.object(store, 'get_merchant', return_value=None)
            mocked_update_merchant = mocker.patch.object(store, 'update_merchant', return_value=fake_merchant_obj)
            result = controller.update_merchant(merchant_id=merchant_id, body=new_merchant_details)
            mocked_get_merchant.assert_called_once()
            mocked_get_merchant.assert_called_with(merchant_id=merchant_id)
            mocked_update_merchant.assert_not_called_once()


@pytest.mark.parametrize("merchant_id", [(1)])
def test_delete_merchant_with_valid_merchant_id(mocker, request_context, fake_merchant_obj, merchant_id):
    """ Should delete merchant record for valid merchant id """
    with request_context as r:
        mocked_get_merchant = mocker.patch.object(store, 'get_merchant', return_value=fake_merchant_obj)
        mocked_delete_merchant = mocker.patch.object(store, 'delete_merchant', return_value=None)
        result = controller.delete_merchant(merchant_id=merchant_id)
        mocked_get_merchant.assert_called_once()
        mocked_get_merchant.assert_called_with(merchant_id=merchant_id)
        mocked_delete_merchant.assert_called_once()
        mocked_delete_merchant.assert_called_with(merchant=fake_merchant_obj)


@pytest.mark.parametrize("merchant_id", [(10000)])
def test_delete_merchant_with_invalid_merchant_id(mocker, request_context, fake_merchant_obj, merchant_id):
    """ Should raise Merchant Not Found error for invalid merchant id """
    with request_context as r:
        with pytest.raises(errors.MerchantNotFound):
            mocked_get_merchant = mocker.patch.object(store, 'get_merchant', return_value=None)
            mocked_delete_merchant = mocker.patch.object(store, 'delete_merchant', return_value=None)
            result = controller.delete_merchant(merchant_id=merchant_id)
            mocked_get_merchant.assert_called_once()
            mocked_get_merchant.assert_called_with(merchant_id=merchant_id)
            mocked_delete_merchant.assert_not_called_once()