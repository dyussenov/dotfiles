from fastapi import FastAPI
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

app = FastAPI(title='Fastapi+Tortoise Ecommerce CRUD')

@app.get("/")
async def read_root():
    return {"Hello": "World"}
    
    
register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)