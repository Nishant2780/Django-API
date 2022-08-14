from dataclasses import fields
from rest_framework import serializers
from .models import *

class ProductTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'

class Products_DetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products_Details
        fields = '__all__'        