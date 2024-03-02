from django.urls import path
from django.contrib.auth.decorators import login_required

from orders.views import OrderCreateView, SuccessTemplateView, CancelTemplateView, OrderListView

app_name = 'orders'

urlpatterns = [
    path('order-create/', login_required(OrderCreateView.as_view()), name='order_create'),
    path('', login_required(OrderListView.as_view()), name='orders_list'),
    path('order-success/', login_required(SuccessTemplateView.as_view()), name='order_success'),
    path('order-canceled/', login_required(CancelTemplateView.as_view()), name='order_canceled'),
]
