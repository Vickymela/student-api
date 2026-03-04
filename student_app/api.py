from ninja import NinjaAPI
from .schema import *
from ninja.errors import HttpError

main_api = NinjaAPI()
@main_api.post("createstudent/",response = CreateStudentSchema)
def creatStudent(request,student:CreateStudentSchema):
    if Student.objects.filter(email=student.email).exists():
        raise HttpError(400,"this user already exists")
    new_student = Student.objects.create(
        username= student.username,
        email=student.email,
        year=student.year,
        course=student.course,
    )
    new_student.save()
    return new_student
@main_api.get("getstudents/",response=list[CreateStudentSchema])
def get_students(request):
    students = Student.objects.all()
    return students

@main_api.get("getstudent/{id}/",response=CreateStudentSchema)
def get_student(request,id:int):
    student = Student.objects.get(id=id)
    if student:
        return student
    else:
        raise HttpError(400,"this user does not exist")


@main_api.delete("delete_student/{id}")
def delete_student(request,id:int):
    student = Student.objects.filter(id=id).first()
    if student:
        student.delete()
        return 200,{"user deleted sucessfully"}
    if not student:
        raise HttpError(404,"this user does not exist")
    
@main_api.put("update_student/{id}/",response=CreateStudentSchema)
def update_student(request,student:CreateStudentSchema): 
    existing_student= Student.objects.filter(id=id).first()
    if not existing_student:
         raise HttpError(400,"student not found")
    existing_student.username= student.username,
    if existing_student:
        existing_student.email=student.email,
        existing_student.year=student.year,
        existing_student.course=student.course,
        existing_student.save()
        return existing_student


      
