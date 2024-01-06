from django.urls import path
from .views import *

urlpatterns = [
    path("customer", CustomerDashboard, name="CustomerDashboard"),
    path("customer/request", CreateOrderRequest, name="CreateOrderRequest"),
    path("customer/view", CustomerDashboardView, name="CustomerDashboardView"),
    path("company/report", CompanyReport, name="CompanyDashboardView"),
    path("company/StatusUpdater",
         StatusUpdater, name="StatusUpdaterView"),
    path("company",
         CompanyDashboard, name="CompanyReportView"),
    path("company/reportdata",
         CompanyReportData, name="CompanyReportDataView"),
]
