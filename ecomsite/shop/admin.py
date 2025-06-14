from django.contrib import admin
from .models import Products
from .models import Order
# Register your models here.

admin.site.site_header = "E-Commerce Site"
admin.site.site_title = "E-Commerce Site"
admin.site.index_title ="Manage E-Commerce Site"

admin.site.register(Products)
admin.site.register(Order)