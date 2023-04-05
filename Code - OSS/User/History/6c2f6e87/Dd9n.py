from database import redis_db

class SmsService():
    async def save_code(self, login: str, phone: str, code: int):
        redis_db.hmset(login, {'phone': phone, 'code': code})
    
    async def get_code_by_login(self, login):
        res = redis_db.hgetall(login)
        return res