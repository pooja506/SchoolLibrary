from django.db import models
from account.models import Student
from datetime import datetime,timedelta


# Create your models here.

class Availablebook(models.Model):
    name = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True)
    book_no=models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return self.name

def get_expiry():
    return datetime.today() + timedelta(days=15)

class Issuedbook(models.Model):
    user = models.ForeignKey(Student, null=True, on_delete= models.SET_NULL)
    book =models.ForeignKey(Availablebook, null=True, on_delete= models.SET_NULL, related_name='book' )
    issused_date = models.DateTimeField(auto_now_add=True,null=True)
    deadline=models.DateTimeField(default=get_expiry)

    def __str__(self):
       return str(self.user)
