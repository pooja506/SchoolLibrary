from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from account.models import Student
from user.models import *
from user.mixins import *
from django.views.generic import (DetailView, FormView, ListView, TemplateView,
                                  View)
# Create your views here.

class ViewStudent(LoginRequired404Mixin,SuperuserRequiredMixin,ListView):
    model = Student
    template_name = 'admindata/view_user.html'
    context_object_name = 'contexts'