# Generated by Django 4.2.6 on 2024-02-04 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Категория товаров', 'verbose_name_plural': 'Категории товаров'},
        ),
    ]
