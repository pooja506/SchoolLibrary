from rest_framework import serializers
from account.models import Student
from user.models import Issuedbook, Availablebook

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields=('username','phone_no','address','email')

class IssueBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issuedbook
        exclude = ("user",)

class AvailablebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Availablebook
        fields=('name','author','book_no','price' ,'quantity')