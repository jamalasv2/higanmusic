from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("menghubungkan ke mongo database...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Anon
    LOGGER(__name__).info("berhasil terhubung ke mongo database.")
except:
    LOGGER(__name__).error("gagal menghubungkan ke mongo database.")
    exit()
