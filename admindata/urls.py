from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'admindata'

urlpatterns = [ 
  path('viewstudent/', ViewStudent.as_view(), name='viewstudent'),
]