from django.db import models

from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='Название категории')
    description = models.TextField(null=True, blank=True, verbose_name='Описание категории')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание товара')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество товара на складе')
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.PROTECT,
        related_name='category',
        verbose_name='Категория'
    )

    def __str__(self):
        return self.name


class BasketQuerySet(models.QuerySet):

    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


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
