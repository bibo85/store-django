from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from products.models import Product, ProductCategory, Basket
from users.models import User


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'products/index.html')


def products(request: HttpRequest, category_id=None) -> HttpResponse:
    products = Product.objects.filter(category__id=category_id) if category_id else Product.objects.all()
    context = {
        'title': 'Store - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': products,
    }
    return render(request, 'products/products.html', context=context)


@login_required
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


@login_required
def basket_remove(request: HttpRequest, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
