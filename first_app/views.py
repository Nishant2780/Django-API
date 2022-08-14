from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

# Create your views here.

@api_view(['GET'])
def index(request):
    return Response({"msg": "this is my first api view"}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def prduct_type_api(request):
    if request.method == 'GET':
        data = ProductType.objects.all()

        serializer = ProductTypeSerializers(data, many=True)

        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductTypeSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def products_details_api(request):
    if request.method == 'GET':
        data = Products_Details.objects.all()

        serializer = Products_DetailsSerializers(data, many=True)

        return Response(serializer.data)

    if request.method == 'POST':
        serializer = Products_DetailsSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)            