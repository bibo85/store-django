from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

from products.models import Product, ProductCategory, Basket
from users.models import User


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'products/index.html')


def products(request: HttpRequest) -> HttpResponse:
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context=context)


def basket_add(request: HttpRequest, product_id) -> HttpResponse:
    product = Product.objects.get(pk=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request: HttpRequest, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
