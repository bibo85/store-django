# Generated by Django 4.2.6 on 2024-02-25 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('id',), 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
    ]
