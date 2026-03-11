from typing import List

from ninja import NinjaAPI
from .schema import *
from ninja.errors import HttpError


main_api = NinjaAPI()


@main_api.post("createstudent/", response=ListStudentSchema)
def creatStudent(request, student:CreateEditStudentSchema):

    if Student.objects.filter(email=student.email).exists():
        raise HttpError(400, "This user already exists")
    
    new_student = Student.objects.create(
        username=student.username,
        email=student.email,
        year=student.year,
        course=student.course,
    )
    new_student.save()
    return new_student


@main_api.get("getstudents/", response=List[ListStudentSchema])
def get_students(request):
    students = Student.objects.all()
    return students


@main_api.get("getstudent/{id}/", response=ListStudentSchema)
def get_student(request,id:int):
    student = Student.objects.filter(id=id).first()
    if student:
        return student
    
    raise HttpError(400, "This user does not exist")


@main_api.delete("delete_student/{id}", response=MessageSchema)
def delete_student(request,id:int):
    student = Student.objects.filter(id=id).first()
    if student:
        student.delete()
        return 200, {"detail": "User deleted successfully"}
    
    raise HttpError(404, "This user does not exist")


@main_api.put("students/{student_id}/", response=ListStudentSchema)
def update_student(request, student_id: int, student: CreateEditStudentSchema): 
    existing_student = Student.objects.filter(id=student_id).first()

    if not existing_student:
        raise HttpError(404, "Student not found")

    existing_student.username = student.username
    existing_student.email = student.email
    existing_student.year = student.year
    existing_student.course = student.course

    existing_student.save()

    return existing_student
