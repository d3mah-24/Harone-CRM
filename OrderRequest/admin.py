from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(OrderRequest)
class OrderRequestAdmin(admin.ModelAdmin): 
    list_display = [field.name for field in OrderRequest._meta.get_fields()]