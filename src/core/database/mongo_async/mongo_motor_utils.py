import logging
import os

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from src.core.config import config
from src.core.database.mongo_async.mongo_motor import db


async def connect_to_mongo(_app: FastAPI):
    _app.logger.info("Connecting to database...")
    db.mongo_client = AsyncIOMotorClient(config.MONGO_URI,
                                   maxPoolSize=config.MONGO_MAX_POOL,
                                   minPoolSize=config.MONGO_MIN_POOL)
    _app.logger.info("Connected to database")

async def close_mongo_connection(_app: FastAPI):
    _app.logger.info("Disconnect to database...")
    db.mongo_client.close()