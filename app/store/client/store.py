from app.store.client import service, cache
from app.store.client.model.client import Client
from typing import Optional


def get_client(client_id: str) -> Optional[Client]:
    """ Takes client_id and returns client object if it exists in the database """
    # check cache
    client_cache_result= cache.get_client(client_id=client_id)
    if client_cache_result:
        return Client.from_str(client_cache_result)
    else:
        # query from db
        client_db_result = service.get_client(client_id=client_id)
        if client_db_result:
            # save result to cache
            cache.set_client(client_id=client_id, client_details=client_db_result.to_str())
        return client_db_result