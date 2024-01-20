from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

from products.models import Product, ProductCategory, Basket


class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Store'
        return context


def products(request: HttpRequest, category_id=None) -> HttpResponse:
    products = Product.objects.filter(category__id=category_id) if category_id else Product.objects.all()
    page = request.GET.get(key='page', default=1)
    per_page = 2
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page)
    context = {
        'title': 'Store - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': products_paginator,
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
