import redis
from settings import settings

redis_db = redis.StrictRedis(
    host=settings.redis_host,
    port=settings.redis_port,
    password=None
)
