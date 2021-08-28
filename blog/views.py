from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView,  CreateView, UpdateView, DeleteView, TemplateView
from .models import Post

class PostList(ListView):
    model = Post
    template_name = 'blog/home.html'                  
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPosts(ListView):
    model = Post
    template_name = 'blog/user_posts.html'                  
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetail(DetailView):
    model = Post

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def handle_no_permission(self):
        messages.info(self.request, message='You must be logged in to create a post.')
        return super(PostCreate, self).handle_no_permission()

class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user == self.get_object().author:
            return True
        return False

class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        if self.request.user == self.get_object().author:
            return True
        return False

class AboutView(TemplateView):
    template_name = "blog/about.html"
