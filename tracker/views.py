from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import F
from .models import Post, Comment


def home(request):
    """ Function based view which renders all the tracker posts from tracker database

    App is currently using class view below
    """
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'tracker/home.html', context)



class PostListView(ListView):
    """ Class ListView to display posts from homepage"""
    model = Post
    template_name = 'tracker/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6



class UserPostListView(ListView):
    """ Class ListView to show list of posts for a particular user"""
    model = Post
    template_name = 'tracker/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        """ Get a list of user post objects"""
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    """ Class DetailView to display individual posts"""
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, id=self.kwargs.get('pk'))
        post.inc_view_count()
        post.save()
        return context



class PostCreateView(LoginRequiredMixin, CreateView):
    """ Class CreateView to create new post"""
    model = Post
    fields = ['title', 'content', 'ticket_type', 'status']

    def form_valid(self, form):
        """ Set user to currently logged in user, then validate form"""
        form.instance.author = self.request.user
        return super().form_valid(form)



class CommentCreateView(LoginRequiredMixin, CreateView):
    """ Class CreateView to create new comment"""
    model = Comment
    fields = ['text']

    def form_valid(self, form):
        """ Set user to currently logged in user, then validate form"""
        post = Post.objects.get(id=self.kwargs['pk'])
        form.instance.author = self.request.user
        form.instance.post = post
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Class UpdateView for users to update thier own posts"""
    model = Post
    fields = ['title', 'content', 'ticket_type', 'status']

    def form_valid(self, form):
        """ Set user to currently logged in user, then validate form"""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """ Check to ensure the current user is the author of post"""
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Delete user post, redirect user to homepage"""
    model = Post
    success_url = '/'

    def test_func(self):
        """ Check to ensure the current user is the author of post"""
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request, 'tracker/about.html', {'title':'About'})
