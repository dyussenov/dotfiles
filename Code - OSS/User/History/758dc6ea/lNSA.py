from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Customers(Model):
    name = fields.CharField(max_length=127)
    surname = fields.CharField(max_length=127)
    phone = fields.CharField(max_length=127, unique=True, null=False)
    password = fields.CharField(max_length=127)
    password_hash = fields.CharField(max_length=127, null=True)
    email = fields.CharField(max_length=127, unique=True, null=False)

    class PydanticMeta:
        #exclude = ["password_hash"]
        computed = ["password_hash"]
class Orders(Model):
    customer_id = fields.ForeignKeyField('models.Customers', on_delete='CASCADE')
    order_time = fields.data.DatetimeField(auto_now=True)
    delivery_address = fields.CharField(max_length=127)


class OrdersItems(Model):
    order_id = fields.ForeignKeyField('models.Orders', on_delete='CASCADE')
    item_id = fields.ForeignKeyField('models.Items', on_delete='CASCADE')


class Items(Model):
    name = fields.CharField(max_length=127)
    prince = fields.IntField()
    description = fields.TextField()


AddCustomer = pydantic_model_creator(Customers,name="AddCustomer", exclude_readonly=True)
Customer = pydantic_model_creator(Customers,name="Customer",)