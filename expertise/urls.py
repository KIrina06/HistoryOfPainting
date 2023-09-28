from django.urls import path
from .views import GetOrders, GetOrder, sendText

urlpatterns = [
    path('', GetOrders),
    path('order/<int:id>', GetOrder, name='order_url'),
    path('sendText', sendText, name='sendText'),
]