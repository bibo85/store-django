from django.urls import path

from orders.views import OrderCreateView, SuccessTemplateView, CancelTemplateView, OrderListView

app_name = 'orders'

urlpatterns = [
    path('order-create/', OrderCreateView.as_view(), name='order_create'),
    path('', OrderListView.as_view(), name='orders_list'),
    path('order-success/', SuccessTemplateView.as_view(), name='order_success'),
    path('order-canceled/', CancelTemplateView.as_view(), name='order_canceled'),
]
