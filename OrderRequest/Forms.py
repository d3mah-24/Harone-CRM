# forms.py

from django import forms
from .models import OrderRequest


class OrderRequestForm(forms.ModelForm):
    class Meta:
        model = OrderRequest
        fields = "__all__"
