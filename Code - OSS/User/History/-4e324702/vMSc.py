from fastapi import FastAPI
from api import router
from settings import settings
from fastapi.middleware.cors import CORSMiddleware

tags_metadata = [
    {
        'name': 'users1',
        'description': 'users auth'
    }
]

origins = settings.allowed_urls

app = FastAPI(
    title='Workaus Auth Service',
    description='jwt auth for students and teachers',
    version='1.0.0',
    openapi_tags=tags_metadata,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
