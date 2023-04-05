from fastapi import FastAPI
from api import router
from settings import settings
import settings

tags_metadata = [
    {
        'name': 'users',
        'description': 'users auth'
    }
]

origins = [
    'https://dev.workaus.kz',
    'https://demo.workaus.kz',
    'https://workaus.kz'
]

origins.extend(settings.settings.allowed_urls.split(','))

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
