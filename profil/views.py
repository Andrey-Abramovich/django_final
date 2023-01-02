from django.contrib.auth import login, get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView

from board.models import Post, Respond
from profil.forms import RegisterForm, ConfirmEmailForm, UserUpdateForm
from profil.models import Verification

User = get_user_model()


# def index(request):
#     template_name = 'base.html'
#     return render(request, template_name)
#

# Регистрация пользователя
class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('confirm')


# Подтверждение емейл
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
            code = form.cleaned_data['code']
            user = User.objects.get(email=email)
            ver_user = Verification.objects.get(ver_user=user).ver_code
            if code == ver_user:
                user.is_active = True
                user.save()
                login(request, user)
                return redirect('index')
            else:
                print('RAZNYE')
        context = {
            'form': form
        }
        return render(request, 'registration/confirm.html', context)


# Страница пользователя с отображением постов и откликов
class ProfilDetailView(DetailView):
    model = User
    queryset = User.objects.all()
    template_name = 'profil/profil.html'
    context_object_name = 'profil'

    def get_object(self, **kwargs):
        return get_object_or_404(User, id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        print('context: ', context)
        posts = Post.objects.filter(author=user)
        context['posts'] = posts
        responds = Respond.objects.filter(post__author=user)
        context['responds'] = responds
        return context


# class ProfileTemplateView(TemplateView):
#     template_name = 'profil/profil.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['user'] = User.objects.get(id=self.request.user.id)
#         context['posts'] = Post.objects.filter(author=context['user'])
#         print('context post ', context['posts'])
#         return context


# Заполнение данных пользователя
class ProfilUpdateView(UpdateView):
    form_class = UserUpdateForm
    template_name = 'profil/update.html'
    success_url = reverse_lazy('profil')

    def get_object(self, queryset=None, **kwargs):
        id = self.kwargs.get('pk')
        return User.objects.get(pk=id)
