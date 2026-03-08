from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Register
from .models import Category
from .models import Products

admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Register,UserAdmin)
# Register your models here.
