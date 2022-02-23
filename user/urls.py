from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [ 
  path('viewbook/', Student_viewbook.as_view(), name='student_viewbook'),
  path('viewissuebook/', Student_viewissuebook.as_view(), name='viewissuebook'),

]