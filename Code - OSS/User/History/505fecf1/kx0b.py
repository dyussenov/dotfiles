from tortoise.models import Model
from tortoise import fields

class Task(Model):
    level = fields.IntField(pk=True)
    theory_text = fields.CharField(max_length=1000)
    task_description = fields.CharField(max_length=10000)
    text = fields.DatetimeField(auto_now_add=True)
    expected_result = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.task_description