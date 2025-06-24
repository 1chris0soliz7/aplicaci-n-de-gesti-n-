from django.contrib import admin
from .models import Category
from .models import Stock

admin.site.register(Stock)
admin.site.register(Category)