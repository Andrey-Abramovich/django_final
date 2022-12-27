from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect

from board.models import Respond, Post

User = get_user_model()

@receiver(post_save, sender=Respond)
def respond_save(sender, instance, created, **kwargs):
    respauthor = instance.respauthor
    print('rauthor: ', respauthor)
    post = instance.post.title
    print('rpost : ', post)
    user = instance.post.author
    print('ruser: ', user)
    if created:
        send_mail(
            'fff',
            f'{respauthor} send resp at {post}',
            'admin@site.ru',
            [user.email]
        )
        return redirect('index')


@receiver(post_save, sender=Post)
def post_save(sender, instance, created, **kwargs):
    author = instance.author
    post = instance.title
    users_emails = User.objects.all()
    if created:
        for u in users_emails:
            send_mail(
                'sss',
                f'{author} add a new post {post}',
                'admin@site.ru',
                [u.email]
            )