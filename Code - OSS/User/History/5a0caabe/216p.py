from fastapi import FastAPI
import api
import services
from settings import settings
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tags_metadata = [
    {
        'name': 'manual-search',
        'description': 'teacher search service'
    },

]

app = FastAPI(
    title='Workaus Search Service',
    description='Find teachers by your parameters',
    version='1.0.0',
    openapi_tags=tags_metadata,
)

app.include_router(api.router)