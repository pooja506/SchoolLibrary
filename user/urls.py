from django.contrib import admin
from django.urls import path
from .views import (
  UserDashboard,
  Student_viewbook,
  StudentViewIssueBook,
  PasswordChangeView

)
from django.urls import reverse_lazy

from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [ 
  path('', UserDashboard.as_view(), name='user_dash'),
  path('viewbook/', Student_viewbook.as_view(), name='student_viewbook'),
  path('viewissuebook/<int:pk>/', StudentViewIssueBook.as_view(), name='viewissuebook'),
  path('change-password/',auth_views.PasswordChangeView.as_view( template_name='user/changepassword.html', 
        success_url = reverse_lazy('user:change_password')),name='change_password'),

]