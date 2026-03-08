from django.shortcuts import render
import jwt
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework import permissions
from rest_framework import generics,filters
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.conf import settings
from rest_framework.filters import SearchFilter
from datetime import datetime, timedelta
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Register
from .serializer import Register_serilizer
from .models import Category,Products
from .serializer import category_serilizer,products_serilizer



# ___________________ registeration view _______

class Register_list(ListCreateAPIView):
    queryset=Register.objects.all()
    serializer_class=Register_serilizer
    permission_classes=[permissions.AllowAny]

# _______________ Products API view _________________
class Productlistview(generics.ListCreateAPIView):
    queryset=Products.objects.all()
    serializer_class=products_serilizer
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=['category']
    search_fields=['name']
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Products.objects.all()
    serializer_class=products_serilizer
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes=[permissions.IsAuthenticated]
