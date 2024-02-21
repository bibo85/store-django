from django.urls import path
from django.views.decorators.cache import cache_page

from .views import ProductsListView, basket_add, basket_remove

app_name = 'products'

urlpatterns = [
    path('', cache_page(60 * 30)(ProductsListView.as_view()), name='products-list'),
    path('category/<int:category_id>', cache_page(60 * 30)(ProductsListView.as_view()), name='category-products'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
