from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import Register
from .models import Category
from .models import Products

# ____________________ Registration serilizer___________________
class Register_serilizer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields=['username','email','password']

    def create(self, validated_data):
        validated_data['password']=make_password(validated_data['password'])
        return super().create(validated_data)

# ____________________ product APi serilzier___________________
class category_serilizer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class products_serilizer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields='__all__'
    def validate_price(self,value):
        if value <= 0:
            raise serializers.ValidationError('Price must be greater than zero')
        return value
    def validate_stock(self,value):
        if value == 0:
            raise serializers.ValidationError("Stck must be greater than zero")
        return value
    def validate_name(self,value):
        if Products.objects.filter(name=value).exists():
            raise serializers.ValidationError("Product with this name is already present")

