# Generated by Django 4.2.6 on 2024-02-24 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=64, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=256, verbose_name='Электронная почта')),
                ('address', models.CharField(max_length=256, verbose_name='Адрес доставки')),
                ('basket_history', models.JSONField(default=dict)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('status', models.SmallIntegerField(choices=[(0, 'Создан'), (1, 'Оплачен'), (2, 'В пути'), (3, 'Доставлен')], default=0)),
                ('initiator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
