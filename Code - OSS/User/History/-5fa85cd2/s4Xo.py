from ..database import users_collection
from .. import models
from bson.objectid import ObjectId

def user_helper(user):
    user['id'] = str(user['_id'])
    return user
    



class SearchService:
    async def find_user(self, login: str) -> models.User:
        user = await users_collection.find_one({'login': login})
        return user

    async def find_users(self, tags: list[str]) -> list[models.User]:
        users = []
        for tag in tags:
            print(tag)
            async for user in users_collection.find({'tags': tag}):
                users.append(user)
        return users
    
    async def get_users(self, role: str) -> list[models.User]:
        users = []
        async for user in users_collection.find({'role': role}):
            users.append(user_helper(user))
            print(user['_id'])
        return users
    
    async def get_user(self, user_id: str) -> models.User:
        user = await users_collection.find_one({'_id': ObjectId(user_id)})
        print(user)
        return user

    async def add_user(self, user: models.User):
        await users_collection.insert_one(user_data.dict())
        return 200