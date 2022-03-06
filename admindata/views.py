from re import template
from django.shortcuts import render
from .forms import *
from django.shortcuts import render
from account.models import Student
from user.models import *
from user.mixins import *
from django.views.generic import (DetailView, CreateView, ListView, TemplateView,UpdateView,
                                  DeleteView)
# Create your views here.

class ViewStudent(LoginRequired404Mixin,SuperuserRequiredMixin,ListView):
    model = Student
    queryset = Student.objects.all()
    template_name = 'admindata/view_user.html'
    context_object_name = 'contexts'

class StudentDeleteView(LoginRequired404Mixin,DeleteView):
    template_name = 'admindata/deleteuser.html'
    model = Student
    success_url = reverse_lazy('admindata:viewstudent')
    context_object_name = 'contexts'

class ViewBook(LoginRequired404Mixin,SuperuserRequiredMixin,ListView):
    model = Availablebook
    template_name = 'admindata/view_book.html'
    context_object_name = 'contexts'

class ViewIssueBook(LoginRequired404Mixin,SuperuserRequiredMixin,ListView):
    model = Issuedbook
    template_name = 'admindata/view_issue.html'
    context_object_name = 'contexts'

class ViewDashboard(LoginRequired404Mixin,SuperuserRequiredMixin,TemplateView):
    books = Availablebook.objects.all()
    users = Student.objects.all()
    booksis = Issuedbook.objects.all()
    template_name=('account/admin_dash.html')

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["total_user"] = self.users.count()
        context["total_issue"] = self.booksis.count()
        context["total_book"] = self.books.count()
        return self.render_to_response(context)

class IssueUpdateView(LoginRequired404Mixin,SuperuserRequiredMixin,UpdateView):
    template_name = 'admindata/updateissue.html'
    form_class = IssueForm
    model = Issuedbook
    success_url = reverse_lazy('admindata:admin_dash')

class IssueBookView(LoginRequired404Mixin,SuperuserRequiredMixin,CreateView):
    template_name = 'admindata/updateissue.html'
    form_class = IssueForm
    model = Issuedbook
    success_url = reverse_lazy('admindata:admin_dash')

class IssueDeleteView(LoginRequired404Mixin,DeleteView):
    template_name = 'admindata/deleteiss.html'
    model = Issuedbook
    success_url = reverse_lazy('admindata:viewissuebook')
    context_object_name = 'contexts'

class BookCreateView(LoginRequired404Mixin,CreateView):
    template_name = 'admindata/addbook.html'
    form_class = AddBookForm
    success_url = reverse_lazy('admindata:viewbook')

class BookUpdateView(LoginRequired404Mixin,SuperuserRequiredMixin,UpdateView):
    template_name =  'admindata/addbook.html'
    form_class = AddBookForm
    model = Availablebook
    success_url = reverse_lazy('admindata:viewbook')

class BookDeleteView(LoginRequired404Mixin,DeleteView):
    template_name = 'admindata/delete.html'
    model = Availablebook
    success_url = reverse_lazy('admindata:viewbook')
    context_object_name = 'contexts'