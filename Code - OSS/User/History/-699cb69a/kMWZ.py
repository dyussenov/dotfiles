from database import users_collection
import models

class SearchService:
    async def find_user(self, login: str) -> models.User:
        user = await users_collection.find_one({'login': login})
        print(type(user))
        return user

    async def find_users(self, tags: list[str]) -> list[models.User]:
        users = []
        for tag in tags:
            print(tag)
            async for user in users_collection.find({'tags': tag}):
                users.append(user)
        print(users)
        return users
