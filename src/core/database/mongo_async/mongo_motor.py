from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient


class DataBase:
    mongo_client: AsyncIOMotorClient = None


db = DataBase()


class DataBase1:
    mongo_client: MongoClient = None


db1 = DataBase1()


async def get_database() -> AsyncIOMotorClient:
    return db.mongo_client
