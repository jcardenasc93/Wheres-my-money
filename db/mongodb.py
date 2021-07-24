""" MongoDB configuration """

from motor.motor_asyncio import AsyncIOMotorClient
import logging

from config.db_config import MONGODB_URL, MONGO_DB
from pymongo.errors import InvalidURI, ConnectionFailure


class DBManager:
    """ Connection database manager for mongo """
    def __init__(self):
        self._client: AsyncIOMotorClient = None

    @property
    def client(self):
        return self._client

    async def connect_db(self):
        logging.info("Connecting to database")
        try:
            self._client = AsyncIOMotorClient(str(MONGODB_URL))
        except InvalidURI:
            logging.error("MONGODB_URL not valid, please check your .env file")
        except ConnectionFailure:
            logging.error("Cannot perform the connection to the database")

    async def close_connection(self):
        logging.info("Clossing database connection")
        self._client.close()

    async def get_collection(self, collection: str):
        db = self._client[MONGO_DB]
        return db.get_collection(collection)
