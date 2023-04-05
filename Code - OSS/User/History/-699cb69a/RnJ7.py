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
        fields_to_search = {}
        for f,v in fields.items():
            if v:
                fields_to_search[f] = v
        print(fields)
        async for user in users_collection.find(fields_to_search):
            users.append(user)
        print(users)
        return users
