from fastapi import FastAPI
from . import api

tags_metadata = [
    {
        'name': 'manual-search',
        'description': 'teacher search service'
    },

]

origins = [
    'https://dev.workaus.kz',
    'https://demo.workaus.kz',
    'https://workaus.kz'
]

origins.extend(settings.allowed_urls.split(','))


app = FastAPI(
    title='Workaus Search Service',
    description='Find teachers by your parameters',
    version='1.0.0',
    openapi_tags=tags_metadata,
)

app.include_router(api.router)