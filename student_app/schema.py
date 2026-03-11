
from ninja import ModelSchema,Schema
from .models import *

class CreateEditStudentSchema(ModelSchema):
    class Meta:
        model = Student
        fields = ("username","email","year","course")


class ListStudentSchema(ModelSchema):
    class Meta:
        model = Student
        fields = ("username","email","year","course","id")

class MessageSchema(Schema):
    detail: str
    