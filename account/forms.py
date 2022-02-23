from django import forms
from .models import Student

class StudentSignUpForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['username','email','password','phone_no','address']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())