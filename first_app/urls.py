from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('prduct_type_api', views.prduct_type_api, name="prduct_type_api"),
    path('products_details_api', views. products_details_api, name="products_details_api"),

]
