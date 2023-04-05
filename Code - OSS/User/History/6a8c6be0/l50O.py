from tortoise import Tortoise, run_async


async def connectToDatabase():
    await Tortoise.init(
        db_url='postgres://abu:@127.0.0.1:5432/codequest',
        modules={'models': ['database.models']}
    )

async def main():
    await connectToDatabase()
    await Tortoise.generate_schemas()
    
if __name__ == '__main__':
    run_async(main())