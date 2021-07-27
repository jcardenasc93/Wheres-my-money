""" This module loads and sets all db related configuration """

import os

MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = os.getenv("MONGO_PORT", 27017)
MONGO_USER = os.getenv("MONGO_USER", "mongo_user")
MONGO_PASS = os.getenv("MONGO_PASS", "pass")
MONGO_DB = os.getenv("MONGO_DB", "test")

is_mongo_atlas = True if os.getenv("MONGO_ATLAS",
                                   "False") == str(True) else False

if is_mongo_atlas:
    MONGODB_URL = f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}/{MONGO_DB}"
else:
    MONGODB_URL = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
