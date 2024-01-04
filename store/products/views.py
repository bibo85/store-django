from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'products/index.html')


def products(request: HttpRequest) -> HttpResponse:
    return render(request, 'products/products.html')
