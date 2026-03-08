from django.db import models
from django.contrib.auth.models import AbstractUser


# _________________________ Registeration Model ________________________
class Register(AbstractUser):
    class Meta:
        verbose_name = "Register"          
        verbose_name_plural = "Register"
    
# _________________ Product API Model ________________
class Category(models.Model):
    name=models.CharField()

    def __str__(self):
        return self.name

class Products(models.Model):
    category=models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products'
    )
    name=models.CharField()
    discription=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='products/',null=True, blank=True)
    stock=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# Create your models here.
