from tortoise import Tortoise, run_async
from models import Task
from singleplayer_tasks import tasks

async def connect_to_db():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['models']}
    )

async def add_singlplayers_tasks(tasks: list):
    for task in tasks:
        await Task.create(
            title=task['title'],
            theory_text=task['theory_text'],
            task_description=task['task_description'],
            text=task['text'],
            expected_result=task['expected_result']
        )

async def main():
    await connect_to_db()
    await Tortoise.generate_schemas()
    await add_singlplayers_tasks(tasks)
    
if __name__ == '__main__':
    run_async(main())