from django.urls import path

from .views import (
    product_list)
from . import views


app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product-list')
]
