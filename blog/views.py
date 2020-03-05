from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # redirect, require login
from django.contrib.auth.models import User


'''
posts = [
    {'author': "Albert S.", "title": "Blog Post 1", "content": "First post content", "date_posted":"February 1, 2020"},
    {'author': "Joe D.", "title": "Blog Post 2", "content": "Second post content", "date_posted":"March 1, 2020"},
    {'author': "Will S.", "title": "Blog Post 3", "content": "Third post content", "date_posted":"March 2, 2020"}
]
'''
def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    '''
        Ordering blog posts
    '''
    model = Post
    # <app>/<model?_viewtype>.hmtl
    template_name = 'blog/home.html'
    # Convert list view to post
    context_object_name = 'posts'
    # sort views from newst to oldest
    ordering = ['-date_posted']
    paginate_by = 4

class UserPostListView(ListView):
    '''
        Ordering blog posts
    '''
    model = Post
    # <app>/<model?_viewtype>.hmtl
    template_name = 'blog/user_posts.html'
    # Convert list view to post
    context_object_name = 'posts'
    # sort views from newst to oldest
    #ordering = ['-date_posted']
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    '''
        Working with an individual blog post
    '''
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    '''
        Create new blog
    '''
    model = Post
    fields = ['title', 'content']

    # Overwrite
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''
        Create new blog
    '''
    model = Post
    fields = ['title', 'content']

    # Overwrite
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''
        Working with an individual blog post
    '''
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': "About"})

def contact(requst):
    return HttpResponse("<h2> Contact us.. </h2>")

'''
    Creating class base views, subscibe views in youtube, detail view etc..
'''
