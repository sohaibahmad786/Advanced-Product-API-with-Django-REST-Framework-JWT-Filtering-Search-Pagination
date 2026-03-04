from django.db import models
from django.contrib.auth.models import AbstractUser



class Student(models.Model):
    name=models.CharField()
    email=models.EmailField()
    age=models.IntegerField()
    course=models.CharField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# _________________________ Register Note ________________________
class Register(AbstractUser):
    class Meta:
        verbose_name = "Register"          
        verbose_name_plural = "Register"
    
class Note(models.Model):
    user=models.ForeignKey(Register, on_delete=models.CASCADE)
    title=models.CharField()
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

# Create your models here.
