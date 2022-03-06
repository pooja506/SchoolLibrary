from django.contrib import admin 
from django.urls import path
from api.views import (
    ListIssuedBook,
    ListStudent,
    IssueBook,
    ListAvailableBook,
    AddBook,
    AvailableBookUpdate,
    AvailableBookDelete,
    IssueBookUpdate,
    IssueBookDelete,
    DeleteStudent,
    UpdateStudent,
    CreateStudent,
    )

app_name = 'api'

urlpatterns = [
    path('list/',ListStudent.as_view(), name='student-list'),
    path('list/create',CreateStudent.as_view(), name='student-create'),
    path('list/update/<int:pk>/',UpdateStudent.as_view(), name='student-update'),
    path('list/delete/<int:pk>/',DeleteStudent.as_view(), name='student-delete'),
    path('issuedbooks/list/',ListIssuedBook.as_view(), name='issued-books'),
    path('issuedbooks/create/',IssueBook.as_view(), name='issue-book'),
    path('issuedbooks/update/<int:pk>/',IssueBookUpdate.as_view(), name='issue-bookupdate'),
    path('issuedbooks/delete/<int:pk>/',IssueBookDelete.as_view(), name='issue-bookdelete'),
    path('availablebooks/list/',ListAvailableBook.as_view(), name='available-books'),
    path('availablebooks/create/',AddBook.as_view(), name='add-books'),
    path('availablebooks/update/<int:pk>/',AvailableBookUpdate.as_view(), name='update-books'),
    path('availablebooks/delete/<int:pk>/',AvailableBookDelete.as_view(), name='delete-books'),
]