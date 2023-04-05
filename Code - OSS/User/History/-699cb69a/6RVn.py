from database import users_collection
import models

class SearchService:
    async def find_user(self, login: str) -> models.User:
        user = await users_collection.find_one({'login': login})
        user['_id']=str(user['_id'])
        print(user)
        return user

    async def find_users(self, fields: dict) -> list[models.User]:
        users = []
        for f,v in fields.items():
            if not v:
                del fields[f]
        print(fields)
        async for user in users_collection.find(fields):
            users.append(user)
        print(users)
        return users
