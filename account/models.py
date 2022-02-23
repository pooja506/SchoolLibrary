from django.db import models
from schoollibrary.settings import AUTH_USER_MODEL
from django.contrib.auth.models import User,AbstractUser
# Create your models here.

class Student(AbstractUser):
    phone_no=models.CharField(("Contact Number"),max_length=20,null=True,blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    
    def get_username(self):
        return self.username
