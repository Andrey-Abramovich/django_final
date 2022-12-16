from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='email', max_length=254)
    class Meta:
        model = User
        fields = ['email', 'username']


class ConfirmEmailForm(forms.Form):
    email = forms.EmailField(label='Введите Ваш email', required=True)
    code = forms.CharField(label='Введите проверочный код', required=True)