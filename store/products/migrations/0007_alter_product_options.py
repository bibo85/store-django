# Generated by Django 4.2.6 on 2024-02-21 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_options_alter_productcategory_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('id',), 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
