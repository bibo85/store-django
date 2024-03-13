import stripe
from django.conf import settings
from django.db import models

from users.models import User

stripe.api_key = settings.STRIPE_SECRET_KEY


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='Название категории')
    description = models.TextField(null=True, blank=True, verbose_name='Описание категории')

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание товара')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество товара на складе')
    image = models.ImageField(upload_to='products_images', verbose_name='Изображение', blank=True, null=True)
    stripe_product_price_id = models.CharField(max_length=128, null=True, blank=True, verbose_name='Stripe price_id')
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.PROTECT,
        related_name='category',
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('id',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.stripe_product_price_id:
            stripe_product_price = self.create_stripe_product_price()
            self.stripe_product_price_id = stripe_product_price['id']
        super().save(*args, **kwargs)

    def create_stripe_product_price(self):
        stripe_product = stripe.Product.create(name=self.name)
        stripe_product_price = stripe.Price.create(
            product=stripe_product['id'],
            unit_amount=round(self.price * 100),
            currency='rub',
        )
        return stripe_product_price


class BasketQuerySet(models.QuerySet):

    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)

    def stripe_products(self):
        line_items = []
        for basket in self:
            item = {
                'price': basket.product.stripe_product_price_id,
                'quantity': basket.quantity,
            }
            line_items.append(item)
        return line_items


class Basket(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='user',
    )
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='product',
    )
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    create_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity

    def de_json(self):
        basket_item = {
            'product_name': self.product.name,
            'quantity': self.quantity,
            'price': float(self.product.price),
            'sum': float(self.sum()),
        }
        return basket_item
