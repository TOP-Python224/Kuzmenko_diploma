"""Определяет схемы URL для orders."""

from django.urls import path
from . import views
from orders.views import OrderCreateView, SuccessView, OrderListView, OrderDetailView

app_name = 'orders'

urlpatterns = [
    # Страница заказов
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('orders/', OrderListView.as_view(), name='orders'),
    path('payment/', views.full_fill_order, name='payment'),
    path('success/', SuccessView.as_view(), name='success'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order'),
]

