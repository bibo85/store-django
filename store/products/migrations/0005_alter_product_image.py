# Generated by Django 4.2.6 on 2024-01-18 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_category_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products_images', verbose_name='Изображение'),
        ),
    ]
