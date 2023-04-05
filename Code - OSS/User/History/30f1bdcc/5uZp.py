import motor.motor_asyncio

from . import settings

MONGO_DETAILS = settings.settings.database_url
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.workaus

users_collection = database.get_collection('users')
