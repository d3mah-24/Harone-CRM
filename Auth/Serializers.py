from rest_framework import serializers

from  .models import  Users


class UserSerializers(serializers.ModelSerializer):
    model=Users 
    fields="__all__"