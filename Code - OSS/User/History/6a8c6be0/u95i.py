"""from tortoise import Tortoise, run_async
from config import settings

async def connectToDatabase():
    await Tortoise.init(
        db_url=settings.get_db_uri(),
        modules={'models': ['database.models']}
    )

async def main():
    await connectToDatabase()
    await Tortoise.generate_schemas()
    
if __name__ == '__main__':
    run_async(main())"""