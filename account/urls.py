from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [ 
     path('', views.StudentRegister.as_view(),name='register'),
     path('login/', views.LoginView.as_view(),name='login'),
     path('logout/', views.LogoutView.as_view(), name='logout'),
     path('admin_dash/', views.AdminDash, name='admin_dash'),
     path('user_dash/', views.UserDash, name='user_dash'),

]