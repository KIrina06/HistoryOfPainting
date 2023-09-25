from django.urls import path
from .views import GetOrders, GetOrder

urlpatterns = [
    path('', GetOrders),
    path('order/<int:id>', GetOrder, name='order_url')
]