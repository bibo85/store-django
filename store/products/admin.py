from django.contrib import admin
from .models import Product, ProductCategory, Basket

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', 'image', 'price', 'quantity', 'category')
    search_fields = ('name', 'description')
    ordering = ('-id',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity')
    readonly_fields = ('create_timestamp',)
    extra = 0
