from tortoise.models import Model
from tortoise import fields

class Task(Model):
    level = fields.IntField(pk=True)
    title = fields.CharField(max_length=200)
    theory_text = fields.CharField(max_length=1000)
    task_description = fields.CharField(max_length=10000)
    text = fields.DatetimeField()
    expected_result = fields.DatetimeField()

    def __str__(self):
        return self.title