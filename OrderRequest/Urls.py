from django.urls import path
from .views import *

urlpatterns = [
    path("", CustomerDashboard, name="CustomerDashboard"),
]
