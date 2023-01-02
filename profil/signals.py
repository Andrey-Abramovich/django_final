from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect
from django.utils.crypto import get_random_string

from profil.models import Verification

User = get_user_model()


# Сигнал на создание пользователя
@receiver(post_save, sender=User)
def user_register(sender, instance, created, **kwargs):
    email = instance.email
    # print('email: ', email)
    user = instance
    # print('user: ', user)
    Verification.objects.filter(ver_user=user)
    if created:
        code = get_random_string(10)   # Генерируем рандомный код при создании пользователя
        print('CODE: ', code)
        send_mail('Секретный код автооризации',
                  f'Ваш адрес электронной почты {email} был указан при регистрации. Введите этот код {code} для подтверждения регистрации',
                  'andrey-abtest@yandex.ru',
                  [email])
        Verification.objects.update_or_create(ver_code=code, ver_user=user)
        return redirect('index')
