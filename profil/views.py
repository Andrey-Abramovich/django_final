from django.contrib.auth import login, get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profil.forms import RegisterForm, ConfirmEmailForm
from profil.models import Verification

User = get_user_model()


def index(request):
    template_name = 'base.html'
    return render(request, template_name)


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('confirm')


def confirm_email(request):
    if request.method == 'GET':
        form = ConfirmEmailForm()
        context = {
            'form': form
        }
        return render(request, 'registration/confirm.html', context)
    elif request.method == 'POST':
        form = ConfirmEmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            print('email: ', email)
            code = form.cleaned_data['code']
            print('code: ', code)
            user = User.objects.get(email=email)
            print('user: ', user)
            ver_user = Verification.objects.get(ver_user=user).ver_code
            print('ver_user: ', ver_user)
            if code == ver_user:
                print('uou')
                user.is_active = True
                print('WOW')
                user.save()
                login(request, user)
                return redirect('index')
            else:
                print('RAZNYE')
        context = {
            'form': form
        }
        return render(request, 'registration/confirm.html', context)
