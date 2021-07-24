""" Generic CRUD operations definition """

from config.app_config import AppConfigManager
from pydantic import BaseModel


class CRUDManager:
    """ Manager for perform generic CRUD operations """
    db = AppConfigManager().db

    @classmethod
    async def retrieve_all(cls, collection: str, schema: BaseModel) -> list:
        # First get the collection
        records = []
        async for record in cls.db.get_collection(collection).find():
            records.append(record)
        return records
