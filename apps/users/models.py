from django.db import models

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator 
# Create your models here.

phone_regex = RegexValidator(regex=r'^\+996\d{9}$', message="Номер телефона необходимо ввести в формате: '+996xxxxxxxxx'.")

class User(AbstractUser):

    phone = models.CharField(
        max_length = 255,
        verbose_name = 'Номер телефона'
    )
    age = models.CharField(
        max_length = 255,
        verbose_name = 'Возраст'
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = 'Дата регистрации'
    )

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
