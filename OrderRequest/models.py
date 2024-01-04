from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class OrderRequest(models.Model):
    Customer = models.ForeignKey(User, on_delete=models.CASCADE)
    Deadline = models.DateField()
    Expected_price = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    Price = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    Description = models.CharField(max_length=255, default="")
    Document = models.FileField(upload_to="documents/", blank=True, null=True)
