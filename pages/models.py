from django.db import models
from login.models import Singup
from django.contrib.auth.models import User
# Create your models here.
class tasks(models.Model):
    Title = models.CharField(max_length=1000,blank=False,null=False)
    Description = models.CharField(max_length=1200,blank=False,null=False)
    Date =  models.DateField()
    User_name =  models.ForeignKey(User,on_delete=models.CASCADE,null=True)
