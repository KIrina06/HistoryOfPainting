from django.urls import path
from .views import GetOrders, GetOrder, sendText, delExp

urlpatterns = [
    path('', GetOrders),
    path('order/<int:id>', GetOrder, name='order_url'),
    path('sendText', sendText, name='sendText'),
    path('delExp', delExp, name='delExp'),
]