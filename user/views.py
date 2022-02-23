from django.shortcuts import render
from account.models import Student
from .models import Availablebook, Issuedbook
from .mixins import LoginRequired404Mixin
from django.views.generic import (DetailView, FormView, ListView, TemplateView,
                                  View)
# Create your views here.
class Student_viewbook(ListView):
    model = Availablebook
    template_name = 'user/view_book.html'
    context_object_name = 'contexts'


class Student_viewissuebook(ListView):
    model = Issuedbook
    template_name = 'user/view_issuebook.html'
    context_object_name = 'contexts'