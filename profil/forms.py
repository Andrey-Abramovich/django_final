from datetime import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, SelectDateWidget

User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='email', max_length=254)
    class Meta:
        model = User
        fields = ['email', 'username']


class ConfirmEmailForm(forms.Form):
    email = forms.EmailField(label='Введите Ваш email', required=True)
    code = forms.CharField(label='Введите проверочный код', required=True)


class UserUpdateForm(ModelForm):
    birthday = forms.DateField(label='Дата рождения', initial=datetime.today(),
                               widget=SelectDateWidget(years=range(1950, datetime.today().date().year + 50)))

    class Meta:
        model = User
        fields = ['birthday', 'avatar', 'first_name', 'last_name']

