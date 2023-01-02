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
    url = f'{instance.post.id}'
    if created:
        send_mail(
            'Вы получили отклик на Ваше объявление',
            f'{respauthor} send resp at {post}',
            'admin@site.ru',
            [user.email],
            html_message=f'<a href="http://127.0.0.1:8000/board/post/{url}" role="button">Читать!</a>'
        )
        return redirect('index')
    else:
        send_mail(
            'Ваш отклик принят',
            f'{user} принял Ваш отклик на {post}',
            'admin@site.ru',
            [respauthor.email]
        )
        return redirect('index')


@receiver(post_save, sender=Post)
def post_save(sender, instance, created, **kwargs):
    author = instance.author
    post = instance.title
    url = f'{instance.id}'
    users_emails = User.objects.all()
    if created:
        for u in users_emails:
            send_mail(
                'Появилось новое объявление!',
                f'{author} add a new post {post}',
                'admin@site.ru',
                [u.email],
                html_message=f'<a href="http://127.0.0.1:8000/board/post/{url}" role="button">Читать!</a>'
            )