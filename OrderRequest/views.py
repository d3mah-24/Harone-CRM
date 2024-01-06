from django.shortcuts import render, redirect
from .Forms import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@login_required
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


@login_required
def CustomerDashboard(req):
    return render(req, "CustomerDashboard.Jinja2")


@login_required
def CustomerDashboardView(req):
    ServiceRequests = OrderRequest.objects.filter(Customer=req.user)
    return render(req, "CustomerDashboardView.Jinja2", {"ServiceRequests": ServiceRequests})


@login_required
def CompanyDashboard(req):
    ServiceRequests = OrderRequest.objects.filter(Customer=req.user)
    from itertools import groupby

    def designation_key_func(member): return member.Status
    queryset = OrderRequest.objects.all()

    ServiceRequests = {}
    for k, v in groupby(queryset, designation_key_func):
        ServiceRequests.setdefault(k, []).extend(list(v))
    order = ["New", "Qualified", "Propostion", "Won", "Lost"]
    Sum_tot = {}
    for Status in order:
        if Status not in ServiceRequests:
            ServiceRequests[Status] = []
        Sum_tot[Status] = sum(
            [a.Expected_price for a in ServiceRequests[Status]])
        print(list(ServiceRequests[Status]))
    data = dict(sorted(ServiceRequests.items(),
                key=lambda x:  order.index(x[0])))

    print(data)
    return render(req, "CompanyDashboard.jinja2", {"ServiceRequests": data, "Sum_tot": Sum_tot})


@login_required
def CompanyReportData(req):
    ServiceRequests = OrderRequest.objects.filter(Customer=req.user)
    from itertools import groupby

    def designation_key_func(member): return member.Status
    queryset = OrderRequest.objects.all()

    ServiceRequests = {}
    for k, v in groupby(queryset, designation_key_func):
        ServiceRequests.setdefault(k, []).extend(list(v))
    order = ["New", "Qualified", "Propostion", "Won", "Lost"]
    Sum_tot = {}
    for Status in order:
        if Status not in ServiceRequests:
            ServiceRequests[Status] = []
        Sum_tot[Status] = sum(
            [a.Expected_price for a in ServiceRequests[Status]])

    return JsonResponse(data={"Sum_tot": Sum_tot})


@login_required
@csrf_exempt
def StatusUpdater(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)
            Request = OrderRequest.objects.get(id=data.get("Company_id"))
            Request.Status = data.get("Status")
            Request.save()
            return JsonResponse({'message': 'Data received successfully'})
        except json.JSONDecodeError as e:
            return JsonResponse({'error': f'Invalid JSON format {e}'}, status=400)

    return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


@login_required

def CompanyReport(req):

    return render(req, "CustomerReportView.Jinja2")
