from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, FormView

from board.forms import PostCreateForm, RespondCreateForm
from board.models import Post, Category, Respond


def index(request):
    posts = Post.objects.all()
    category = Category.objects.all()
    respond = Respond.objects.all()
    context = {'posts': posts, 'category': category, 'respond': respond}
    return render(request, 'board/posts.html', context)


class PostCreate(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'board/postcreate.html'
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class PostDetail(DetailView, FormView):
    model = Post
    form_class = RespondCreateForm
    success_url = reverse_lazy('profil')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['responds'] = Respond.objects.filter(post__id=self.object.id)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.respauthor = self.request.user
        print('author: ', self.object.respauthor)
        print('user: ', self.request.user)
        # достаю и переопределяю id
        id = self.kwargs.get('pk')
        # привязываю комментарий к посту
        self.object.post_id = id
        self.object.save()
        return super().form_valid(form)


class RespondCreate(CreateView):
    model = Post
    form_class = RespondCreateForm
    template_name = 'board/respond_create.html'
    success_url = reverse_lazy('post_detail')


    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id = self.object.get('pk')
        self.object.post_id = id
        self.object.respauthor = self.request.user
        self.object.save()
        return super().form_valid(form)
