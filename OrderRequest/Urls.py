from django.urls import path
from .views import *

urlpatterns = [
    path("", CustomerDashboard, name="CustomerDashboard"),
    path("request", CreateOrderRequest, name="CreateOrderRequest"),
    path("view", CustomerDashboardView, name="CustomerDashboardView"),
]
