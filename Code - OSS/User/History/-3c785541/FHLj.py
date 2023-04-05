from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from settings import settings


tags_metadata = [
    {
        'name': 'text',
        'description': 'text content for landing page'
    }
]

app = FastAPI(
    title='Workaus Content Service',
    description='Gives text and media content to frontend',
    version='1.0.0',
    openapi_tags=tags_metadata,
)
print(settings.allowed_urls)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

