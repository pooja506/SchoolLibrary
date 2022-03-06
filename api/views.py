from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from  .serializers import (IssueBookSerializer, 
StudentSerializer,
AvailablebookSerializer,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from account.models import Student
from user.models import Issuedbook, Availablebook


class ListStudent(ListAPIView):
    queryset= Student.objects.all()
    serializer_class= StudentSerializer
    permission_classes = (AllowAny,)

class UpdateStudent(UpdateAPIView):
    serializer_class = StudentSerializer
    queryset =  Student.objects.all()
    permission_classes = (IsAuthenticated, )
    
class CreateStudent(CreateAPIView):
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated,)

class DeleteStudent(DestroyAPIView):
    queryset = Student.objects.all()
    permission_classes = (IsAuthenticated, )

class ListIssuedBook(ListAPIView):
    queryset= Issuedbook.objects.all()
    serializer_class= IssueBookSerializer
    permission_classes = (AllowAny, )

class IssueBook(CreateAPIView):
    serializer_class = IssueBookSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self,serializer):
        serializer.save(user =(self.request.user))  

class IssueBookUpdate(UpdateAPIView):
    serializer_class = IssueBookSerializer
    queryset =  Issuedbook.objects.all()
    permission_classes = (IsAuthenticated, )


class IssueBookDelete(DestroyAPIView):
    queryset = Issuedbook.objects.all()
    permission_classes = (IsAuthenticated, )

class ListAvailableBook(ListAPIView):
    queryset= Availablebook.objects.all()
    serializer_class= AvailablebookSerializer
    permission_classes = (AllowAny, )

class AddBook(CreateAPIView):
    serializer_class = AvailablebookSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self,serializer):
        serializer.save()  

class AvailableBookUpdate(UpdateAPIView):
    serializer_class = AvailablebookSerializer
    queryset = Availablebook.objects.all()
    permission_classes = (IsAuthenticated, )

class AvailableBookDelete(DestroyAPIView):
    queryset = Availablebook.objects.all()
    permission_classes = (IsAuthenticated, )