from django.urls import path
from .views import *

urlpatterns = [
    path("", Index, name="Index"),
    path("register", UserRegister, name="Register"),
    path("login", UserLogin, name="Login"),
    path("logout", UserLogout, name="Logout"),
]
