import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
import logging

from app.config import Config

load_dotenv()

db_client: AsyncIOMotorClient = None


async def get_db() -> AsyncIOMotorClient:
    db_name = Config.app_settings.get("db_name")
    return db_client[db_name]


async def connect_and_init_db():
    global db_client
    try:
        db_client = AsyncIOMotorClient(Config.MONGO_CONN)
        logging.info("Connected to mongo.")
    except Exception as e:
        logging.exception(f"Could not connect to mongo: {e}")
        raise


async def close_db_connect():
    global db_client
    if db_client is None:
        logging.warning("Connection is None, nothing to close.")
        return
    db_client.close()
    db_client = None
    logging.info("Mongo connection closed.")
