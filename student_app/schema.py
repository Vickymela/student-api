
from ninja import ModelSchema,Schema
from .models import *

class CreateStudentSchema(ModelSchema):
    class Meta:
        model = Student
        fields = ("username","email","year","course")
class OutputCreateStudentSchema(ModelSchema):
    class Meta:
        model = Student
        fields = ("username","email","year","course","id")
class RegisterSchema(Schema):
    username: str
    email: str
    password: str
class ReturnedRegisterSchema(ModelSchema):
    class Meta:
        model = User
        fields = ("username","email")
class LoginSchema(Schema):
    username: str
    password: str
class OutputLoginSchema(ModelSchema):
    class Meta:
        model = User
        fields = ("username",)
class Outputgetallstudents(ModelSchema):
    class Meta:
        model = User
        fields =("username","email","password")
    