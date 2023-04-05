from database import redis_db

class SmsService():
    async def save_code(self, login: str, phone: str, code: int):
        redis_db.hmset(login, {'phone': phone, 'code': code})
    
    async def get_codes(self, login):
        res = redis_db.hmget(login, {})
        return res