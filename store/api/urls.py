from django.urls import path

from api.views import ProductListApiView

name = "api"

urlpatterns = [
    path('product-list/', ProductListApiView.as_view(), name='api_product_list'),
]
