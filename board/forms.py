from django.forms import ModelForm

from board.models import Post


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'roles', 'upload']
