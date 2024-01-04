# from rest_framework import generics
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .Forms import *


def UserRegister(req):
    if not req.user.is_authenticated:
        if req.method == "POST":
            form = UsersForm(req.POST)
            print(form.is_valid())
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = 1
                user.set_password(form.cleaned_data["password"])
                user.save()
                # print()
                return redirect("Login")
            print(form.errors.as_data())
            return render(req, "Register.jinja2", {"form": form})

        else:
            return render(req, "Register.jinja2")
    else:
        return redirect("/")


def UserLogin(req):
    if not req.user.is_authenticated:
        if req.method == "POST":
            email = req.POST.get("email")
            password = req.POST.get("password")
            user = authenticate(req, email=email, password=password)
            print(email, password)
            print(user)
            if user is not None:
                login(req, user)
                return redirect("/")
            else:
                return render(req, "Login.jinja2", {"wrong_pass": True})
        else:
            return render(req, "Login.jinja2")
    else:
        return redirect("/")


def UserLogout(request):
    logout(request)
    return redirect("/")


def Index(req):
    if req.user.is_authenticated:
        return render(req, "Home.jinja2", {"data": [98, 8]})
    return render(req, "Index.jinja2", {"data": [98, 8]})
