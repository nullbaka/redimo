import os
from dotenv import load_dotenv

env = load_dotenv()


class Config:
    CACHE_HOST = os.getenv("CACHE_HOST")
    CACHE_PORT = int(os.getenv("CACHE_PORT"))
    SECRET_KEY = os.getenv("SECRET_KEY")

    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
    JWT_EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES"))

    MONGO_HOST = os.getenv("MONGO_HOST")
    MONGO_USER = os.getenv("MONGO_USER")
    MONGO_PASS = os.getenv("MONGO_PASS")
    MONGO_CONN = f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}"

    DB_NAME = os.getenv("DB_NAME")
    DB_COLLECTION = os.getenv("nullcollection")
