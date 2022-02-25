from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


app_name = 'admindata'

urlpatterns = [ 
    path('', ViewDashboard.as_view(), name='admin_dash'),
    path('viewstudent/', ViewStudent.as_view(), name='viewstudent'),
    path('deletestudent/<int:pk>/', StudentDeleteView.as_view(), name='deletestudent'),
    path('viewbook/', ViewBook.as_view(), name='viewbook'),
    path('viewissuebook/', ViewIssueBook.as_view(), name='viewissuebook'),
    path('addbook/', BookCreateView.as_view(), name='addbook'),
    path('issuebook/', IssueBookView.as_view(), name='issuebook'),
    path('updateissue/<int:pk>/', IssueUpdateView.as_view(), name='updateissue'),
    path('deleteissue/<int:pk>/', IssueDeleteView.as_view(), name='deleteissue'),
    path('updatebook/<int:pk>/', BookUpdateView.as_view(), name='updatebook'),
    path('deletebook/<int:pk>/', BookDeleteView.as_view(), name='deletebook'),
    path('changepassword/',auth_views.PasswordChangeView.as_view( template_name='user/changepassword.html', 
        success_url = reverse_lazy('user:change_password')),name='change_password'),
]