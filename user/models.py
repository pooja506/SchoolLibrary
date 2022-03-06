from django.db import models
from account.models import Student
from django.db.models.signals import post_save, pre_delete
from datetime import datetime,timedelta
from django.dispatch import receiver

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
    

    @property
    def deadline_expire(self):
        dead= self.deadline
        expire = "Expired"
        naive = dead.replace(tzinfo=None)
        diff=datetime.today() - naive
        if diff.days>0:
            return expire
        else:
            return dead

    @property
    def date_diff(self):
        expire = self.deadline
        naive = expire.replace(tzinfo=None)
        diff = naive - datetime.today()
        return diff.days

    @property
    def fine(self):
        fine=0
        if self.date_diff<0:
            fine=abs(self.date_diff)*10 
        return abs(fine)

        
@receiver(post_save,sender=Issuedbook)
def bookscount(sender,instance,created,**kwargs):
	
	if created:
		book = Availablebook.objects.get(id=instance.book.id)
		book.quantity = int(book.quantity) - 1
		book.save()

@receiver(pre_delete,sender=Issuedbook)
def bookscountadd(sender,instance,**kwargs):
	book = Availablebook.objects.get(id=instance.book.id)
	book.quantity = int(book.quantity) + 1
	book.save()

