from django.urls import path

from .views import products, basket_add

app_name = 'products'

urlpatterns = [
    path('', products, name='products-list'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
]
