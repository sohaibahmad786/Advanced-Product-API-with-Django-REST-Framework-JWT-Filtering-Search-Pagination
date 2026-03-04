from django.shortcuts import render
import jwt
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework import permissions,generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Student
from .serializer import Student_serilizer
from django.conf import settings
from datetime import datetime, timedelta
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Register
from .serializer import Register_serilizer
from .models import Note
from .serializer import Note_serilizer


  
# ______________________ Student Managment API___________________
class student_list(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=Student_serilizer
class student_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=Student_serilizer
    

# _____________________ Banking Account API __________
# class account_list(generics.ListCreateAPIView):
#     queryset=Account.objects.all()
#     serializer_class=Account_serilizer
#     authentication_classes=[JWTAuthentication]
#     permission_classes=[permissions.AllowAny]

# class account_detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Account.objects.all()
#     serializer_class=Account_serilizer
#     authentication_classes=[JWTAuthentication]
#     permission_classes=[permissions.AllowAny]


# ___________________ register________

class Register_list(ListCreateAPIView):
    queryset=Register.objects.all()
    serializer_class=Register_serilizer
    permission_classes=[permissions.AllowAny]


class Note_list(generics.ListCreateAPIView):

    queryset=Note.objects.all()
    serializer_class=Note_serilizer
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
   
class Note_detail(generics.RetrieveUpdateDestroyAPIView):

    queryset=Note.objects.all()
    serializer_class=Note_serilizer
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes=[permissions.IsAuthenticated]

