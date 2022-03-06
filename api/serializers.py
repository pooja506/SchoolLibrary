from rest_framework import serializers
from account.models import Student
from user.models import Issuedbook

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields=('username','phone_no','address','email')

class IssueBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issuedbook
        exclude = ("user",)
