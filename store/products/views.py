from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from products.models import Product, ProductCategory


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'products/index.html')


def products(request: HttpRequest) -> HttpResponse:
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context=context)
