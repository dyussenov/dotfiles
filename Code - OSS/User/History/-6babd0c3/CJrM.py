from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from settings import settings
from api import router

tags_metadata = [
    {
        'name': 'Auth SMS',
        'description': 'SMS for authentication'
    }
]

app = FastAPI(
    title='SMS service',
    description='SMS management for Workaus',
    version='1.0.0',
    openapi_tags=tags_metadata,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_urls,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
