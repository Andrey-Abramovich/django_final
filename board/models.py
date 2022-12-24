from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=128, verbose_name="Заголовок")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    roles = models.ForeignKey("Category", on_delete=models.CASCADE, blank=True)
    upload = models.FileField(upload_to='uploads/', null=True)

    def __str__(self):
        return '{}'.format(self.title)


class Category(models.Model):
    name = models.CharField(max_length=28, unique=True, verbose_name='Название')

    def __str__(self):
        return '{}'.format(self.name)


class Respond(models.Model):
    respauthor = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=False)
    dateCreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.text)
