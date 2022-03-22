from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email =models.EmailField(unique=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=15)
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name