from django.contrib.auth import login
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profil.forms import RegisterForm


def index(request):
    template_name = 'base.html'
    return render(request, template_name)

class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterForm

    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = form.save()
            login(request, user)
            send_mail('subject',
                'message',
                'admin@site.ru',
                [email])
            return redirect('index')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)



