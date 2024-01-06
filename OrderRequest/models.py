from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class OrderRequest(models.Model):
    Customer = models.ForeignKey(User, on_delete=models.CASCADE)
    Deadline = models.DateField()
    Expected_price = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    Price = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    Description = models.CharField(max_length=255, default="")
    Document = models.FileField(upload_to="documents/", blank=True, null=True)
    Date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    Status = models.CharField(
        max_length=200, default="New", blank=True, null=True)
