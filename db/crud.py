""" Generic CRUD operations definition """

from config.app_config import AppConfigManager
from pydantic import BaseModel


class CRUDManager:
    """ Manager for perform generic CRUD operations """
    db_client = AppConfigManager().db

    @classmethod
    async def find_all(cls, collection: str, model: object) -> list:
        # First get the collection
        documents = []
        if type(model) == type(BaseModel):
            conn = cls.db_client.collection(collection).find()
            for document in await conn.to_list(length=10):
                documents.append(document)
        else:
            raise ValueError("Model not valid")

        return documents

    @classmethod
    async def find_one(cls, collection: str, model: object,
                       query: dict) -> list:
        # First get the collection
        if type(model) == type(BaseModel):
            document = await cls.db_client.collection(collection).find_one(
                query)
            return document
        else:
            raise ValueError("Model not valid")
