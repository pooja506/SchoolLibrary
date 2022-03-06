from django.contrib import admin 
from django.urls import path
from api.views import (
    ListIssuedBook,
    ListStudent,
    IssueBook
    )

app_name = 'api'

urlpatterns = [
    path('list/',ListStudent.as_view(), name='student_list'),
    path('issuedbooks/list/',ListIssuedBook.as_view(), name='issued-books'),
    path('issuedbooks/create/',IssueBook.as_view(), name='issue_book'),
]
