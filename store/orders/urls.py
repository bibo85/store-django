from django.contrib.auth.decorators import login_required
from django.urls import path

from orders.views import (CancelTemplateView, OrderCreateView, OrderDetailView,
                          OrderListView, SuccessTemplateView)

app_name = 'orders'

urlpatterns = [
    path('order-create/', login_required(OrderCreateView.as_view()), name='order_create'),
    path('', login_required(OrderListView.as_view()), name='orders_list'),
    path('order/<int:pk>', login_required(OrderDetailView.as_view()), name='order_detail'),
    path('order-success/', login_required(SuccessTemplateView.as_view()), name='order_success'),
    path('order-canceled/', login_required(CancelTemplateView.as_view()), name='order_canceled'),
]
