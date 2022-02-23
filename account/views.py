from django.shortcuts import render, redirect
from django.views import generic
from .forms import *
from django.urls import  reverse_lazy
from django.contrib.auth import authenticate, login, logout
from account.models import Student


# Create your views here.
class StudentRegister(generic.CreateView):
    # model = Student
    form_class = StudentSignUpForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('admin_dash')

    def form_valid(self, form):
        form.save()
        return redirect('login')

class LoginView(generic.FormView):
    def get(self,*args,**kwargs):
        form = LoginForm()
        return render(self.request,'account/login.html',{'form':form})
        
    def post(self,*args,**kwargs):
        form = LoginForm(self.request.POST)
        print(form.data,"test")
        if form.is_valid():
            username = form.data.get('username')
            password = form.data.get('password')
            user = authenticate(self.request,username = username,password = password)
            if user:
              login(self.request, user)
              if self.request.user.is_superuser:
                return redirect('admin_dash')
              else:
                return redirect('user_dash')
        else:
            return render(
                self.request,
                self.template_name,
                 {"error": "Your Username or Password do not match.", "form": form},
            )          

class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy("login"))

def UserDash(request):
    return render(request, 'account/user_dash.html')

def AdminDash(request):
    return render(request, 'account/admin_dash.html')