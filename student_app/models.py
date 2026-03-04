from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    year = models.IntegerField()
    course = models.CharField( max_length=50)

    def __str__(self):
        return f"{self.name} - {self.email}"