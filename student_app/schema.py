
from ninja import ModelSchema,Schema
from .models import *

class CreateStudentSchema(ModelSchema):
    class Meta:
        model = Student
        fields = ("username","email","year","course","id")