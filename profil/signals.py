from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect
from django.utils.crypto import get_random_string

from profil.models import Verification

User = get_user_model()


@receiver(post_save, sender=User)
def user_register(sender, instance, **kwargs):
    print('instance ', instance)
    email = instance.email
    print('email: ', email)
    user = instance
    print('user: ', user)
    v = Verification.objects.filter(ver_user=user)
    print('v: ', v)
    if v.exists():
        print('TRUUUUUUE!!!')
        return redirect('index')

    else:
        code = get_random_string(10)
        print('CODE: ', code)
        send_mail('Enter this secret code to confirm your email',
                  f'Your code: {code}',
                  'admin@site.ru',
                  [email])
        V = Verification.objects.update_or_create(ver_code=code, ver_user=user)
        return redirect('index')
