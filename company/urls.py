from django.urls import path, include
from . import views

urlpatterns = [
    path('customer/', views.customer, name='customer'),
    path('customer/<int:conum>', views.edit_customer, name='customer_edit')
    ]
