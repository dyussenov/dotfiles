import redis

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Response



r = redis.StrictRedis(
    host='redis-17449.c55.eu-central-1-1.ec2.cloud.redislabs.com',
    port=17449,
    password='qwerty'
)

router = APIRouter(
    prefix='/notification',
    tags=['notification'],
)