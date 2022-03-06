from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from  .serializers import IssueBookSerializer, StudentSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from account.models import Student
from user.models import Issuedbook


class ListStudent(ListAPIView):
    queryset= Student.objects.all()
    serializer_class= StudentSerializer
    permission_classes = (AllowAny, )

class ListIssuedBook(ListAPIView):
    queryset= Issuedbook.objects.all()
    serializer_class= IssueBookSerializer
    permission_classes = (AllowAny, )

class IssueBook(CreateAPIView):
    serializer_class = IssueBookSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self,serializer):
        print("test")
        print(self.request.user)
        serializer.save(user =(self.request.user))  
