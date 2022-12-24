from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from board.forms import PostCreateForm
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

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
