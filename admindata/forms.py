from email import message
from user.models import Availablebook, Issuedbook
from django.forms import ModelForm



class IssueForm(ModelForm):
    class Meta:
        model = Issuedbook
        fields = '__all__'

class AddBookForm(ModelForm):
    class Meta:
        model = Availablebook
        fields = '__all__'