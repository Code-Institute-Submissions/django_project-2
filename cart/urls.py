from django.urls import path

from .views import (
    add_to_cart,
    delete_from_cart,
    order_details,
    checkout,
    update_transaction_records,
    success
)
from . import views

app_name = 'cart'

urlpatterns = [
    path('add-to-cart/<item_id>/', views.add_to_cart, name="add_to_cart"),
    path('order-summary/', views.order_details, name="order_summary"),
    path('success/', views.success, name='purchase_success'),
    path('item/delete/<item_id>/', views.delete_from_cart, name='delete_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('update-transaction/<token>/', views.update_transaction_records,
        name='update_records')
]
