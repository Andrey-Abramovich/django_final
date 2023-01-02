from django.forms import ModelForm

from board.models import Post, Respond


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'roles', 'upload']


class RespondCreateForm(ModelForm):
    class Meta:
        model = Respond
        fields = ['text']