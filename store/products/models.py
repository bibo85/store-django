from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='Название категории')
    description = models.TextField(null=True, blank=True, verbose_name='Описание категории')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание товара')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество товара на складе')
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.PROTECT,
        related_name='category',
    )

    def __str__(self):
        return {self.name}
