# Generated by Django 4.2.6 on 2024-02-04 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_verified_email_emailverification'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailverification',
            options={'verbose_name': 'Подтверждение почты', 'verbose_name_plural': 'Подтверждение почты'},
        ),
    ]
