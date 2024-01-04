from django.shortcuts import render, redirect

from .Forms import *


# Create your views here.
def CreateOrderRequest(request):
    print(request.POST, request.FILES)
    if request.method == "POST":
        request.POST._mutable = True
        request.POST["Customer"] = request.user
        request.POST._mutable = False

        form = OrderRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "CustomerDashboard.Jinja2", {"success": 1})
    else:
        return redirect("/customer")

    print(form.errors.as_data())
    return render(request, "CustomerDashboard.Jinja2", {"form": form})


def CustomerDashboard(req):
    return render(req, "CustomerDashboard.Jinja2")


def CustomerDashboardView(req):
    ServiceRequests= OrderRequest.objects.filter(Customer=req.user)
    
    return render(req, "CustomerDashboardView.Jinja2",{"ServiceRequests":ServiceRequests})
