from database import redis_db

class SmsService():
    async def save_code(self, login: str, phone: str, code: int):
        redis_db.hmset(login, {'phone': phone, 'code': code})
    
    async def get_code_by_login(self, login):
        res = redis_db.hgetall(login)
        return res

    async def check_sms_code(self, login: str, code: int):
        res = redis_db.hgetall(login)
        print(res)
        if res == {}:
            return None
        print(res[b'code']) 
        print(res[b'code'].decode("utf-8"))
        if res[b'code'].decode("utf-8") == code:
            print('c')