import redis

from config import settings

redis_db = redis.StrictRedis(
    host=settings.redis_host,
    port=settings.redis_port,
    password=None
)