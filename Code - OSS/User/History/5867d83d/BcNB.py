import redis

from config import settings

redis_db = redis.StrictRedis(
    host=settings.REDIS_URL,
    port=settings.REDIS_PORT,
    password=None
)