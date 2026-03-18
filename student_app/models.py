from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    year = models.IntegerField()
    course = models.CharField( max_length=50)

    def __str__(self):
        return f"{self.name} - {self.email}"