from fastapi import FastAPI
from api import router
from settings import settings
tags_metadata = [
    {
        'name': 'users',
        'description': 'users auth'
    }
]

app = FastAPI(
    title='Workaus Auth Service',
    description='jwt auth for students and teachers',
    version='1.0.0',
    openapi_tags=tags_metadata,
)

app.include_router(router)
print(settings.database_password, settings.database_login)