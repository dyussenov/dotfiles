from database import redis_db

class SmsService():
    async def save_code(self, login: str, phone: str, code: int):
        redis_db.set(login, code)
        res = redis_db.get(login)
        print(res)