from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True, verbose_name='Аватар пользователя')
    is_verified_email = models.BooleanField(default=False, verbose_name='Статус подтверждения email')


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True, verbose_name='Код для подтверждения email')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    expiration = models.DateTimeField(verbose_name='Дата окончания')

    def __str__(self):
        return f'EmailVerification object for {self.user.email}'
