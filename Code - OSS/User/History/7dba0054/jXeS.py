import redis

import motor.motor_asyncio

from settings import settings

MONGO_DETAILS = settings.database_url
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.workaus

users_collection = database.get_collection('users')
courses_collection = database.get_collection('courses')
lessons_collection = database.get_collection('lessons')

redis_db = redis.StrictRedis(
    host=settings.redis_host,
    port=settings.redis_port,
    password=None
)

