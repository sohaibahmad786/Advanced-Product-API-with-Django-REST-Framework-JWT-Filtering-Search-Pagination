from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import Register_list
from .views import Productlistview,ProductDetail


urlpatterns = [
    path('login/',TokenObtainPairView.as_view()),
    path('login/refresh/',TokenRefreshView.as_view()),
    path('register/',Register_list.as_view()),
    path('product/',Productlistview.as_view()),
    path('product/<int:pk>/',ProductDetail.as_view()),

]
