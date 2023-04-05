from fastapi import FastAPI
import api
import services

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