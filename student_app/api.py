# from urllib import request

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from django.contrib.auth import authenticate, login as auth_login
from .schema import *
from ninja.errors import HttpError
from django.contrib.auth.hashers import make_password
from ninja.security import django_auth
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt

main_api = NinjaAPI()
# register
# login 
# logout
# authentication

@main_api.post("register/",response = ReturnedRegisterSchema)
def register(request,register:RegisterSchema):
    if User.objects.filter(email=register.email).exists():
        raise HttpError(400,"THIS USER ALREADY EXISTS")
    if User.objects.filter(username=register.username).exists():
        raise HttpError(400,"THIS USER ALREADY EXISTS")
    if register:
        registered_student = User.objects.create(
            username = register.username,
            email = register.email,
            password = make_password(register.password)
            
        )
    
        #rember to ask why the first one is not working
        # return {f"user created sucessfully {registered_student.username}\n {registered_student.email}"}
        return registered_student
    
@main_api.post("login/",response=OutputLoginSchema)
def login_view(request,logged_in_user:LoginSchema):
  user =authenticate(request,username=logged_in_user.username,password=logged_in_user.password)
  if user is None:
      raise HttpError(400,"invalid username or password") 
  auth_login(request,user)
  return user

@main_api.get("logout/",auth=django_auth)
def logout_view(request):
    # if request.auth():  current logged in user
        logout(request)
        return {"message":"logout sucessful"}


@main_api.post("createstudent/",response = OutputCreateStudentSchema,auth=django_auth)
@csrf_exempt
def creatStudent(request,student:CreateStudentSchema):
        if Student.objects.filter(email=student.email).exists():
            raise HttpError(400,"this user already exists")
        new_student = Student.objects.create(
            user= request.auth,
            username= student.username,
            email=student.email,
            year=student.year,
            course=student.course,
        )
        new_student.save()
        return new_student

# this is not working omogi
@main_api.get("getstudent/{id}/",response=CreateStudentSchema,auth=django_auth)
@csrf_exempt
def get_student(request,id:int):
    student = get_object_or_404(Student, id=id)
    current_user = request.auth
    if current_user != student.user:
         raise HttpError(400,"your not authorized to see this user")
        
    return student
    

@main_api.delete("delete_student/{id}",auth=django_auth)
@csrf_exempt
def delete_student(request,id:int):
    student = Student.objects.filter(id=id).first()
    if not student:
        raise HttpError(404,"this user does not exist")
    student.delete()
    return {"user deleted sucessfully"}
  
    

    

@main_api.put("students/{student_id}/", response=CreateStudentSchema,auth=django_auth)
@csrf_exempt
def update_student(request, student_id: int, student: CreateStudentSchema): 

    existing_student = Student.objects.filter(id=student_id).first()

    if not existing_student:
        raise HttpError(404, "Student not found")

    existing_student.username = student.username
    existing_student.email = student.email
    existing_student.year = student.year
    existing_student.course = student.course

    existing_student.save()

    return existing_student


      
