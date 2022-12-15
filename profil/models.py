from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    birthday = models.DateField(blank=True, null=True, verbose_name='дата рождения')
    avatar = models.ImageField(upload_to='avatars/%Y/%m/%d', blank=True, null=True, verbose_name='аватарка')
    email = models.EmailField(unique=True, blank=True, verbose_name='email')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
