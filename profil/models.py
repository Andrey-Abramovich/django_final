from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

class User(AbstractUser):
    birthday = models.DateField(blank=True, null=True, verbose_name='дата рождения')
    avatar = models.ImageField(upload_to='avatars/%Y/%m/%d', blank=True, null=True, verbose_name='аватарка')
    email = models.EmailField(unique=True, blank=True, verbose_name='email')
    is_active = models.BooleanField(
        _("active"),
        default=False,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


class Verification(models.Model):
    ver_code = models.CharField(max_length=10)
    ver_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ver_user
