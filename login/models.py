from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Singup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname  = models.CharField(max_length=1000)
    gender = models.CharField(max_length=6, choices=[("male", "Male"), ("female", "Female")])

    def __str__(self):
        return self.fullname

