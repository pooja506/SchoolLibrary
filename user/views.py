from .models import Availablebook, Issuedbook
from .mixins import LoginRequired404Mixin
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView, 
    ListView, 
    TemplateView
    )
# Create your views here.
class Student_viewbook(LoginRequired404Mixin,ListView):
    model = Availablebook
    template_name = 'user/view_book.html'
    context_object_name = 'contexts'


class StudentViewIssueBook(LoginRequired404Mixin,DetailView):
    model = Issuedbook
    template_name = 'user/view_issuebook.html'
    context_object_name = 'contexts'

class PasswordChangeView(LoginRequired404Mixin):
        template_name='user/changepassword.html', 
        success_url = reverse_lazy('user:change_password')

class UserDashboard(LoginRequired404Mixin,TemplateView):
    template_name='account/user_dash.html'

        
        