import motor.motor_asyncio

import settings

MONGO_DETAILS = settings.settings.database_url
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.workaus
print(settings.settings.database_url)
users_collection = database.get_collection('users')
