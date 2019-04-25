from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView
from django.db.models import Count, Q
from .models import Post, Comment


def home(request):
    """ Function based view which renders all the tracker posts from tracker database

    App is currently using class view below
    """
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'tracker/home.html', context)


class ChartData(APIView):
    """
    Django Rest APIView
    View to get bug and feature data for rendering charts with Chart JS
    Using Ajax calls on front end to render data driven charts
    """
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        bugs = Post.objects.filter(ticket_type='BG')\
        .annotate(num_upvotes=Count('upvotes')).order_by('-num_upvotes')[:10]

        features = Post.objects.filter(ticket_type='FT')\
        .annotate(num_upvotes=Count('upvotes')).order_by('-num_upvotes')[:10]

        bug_labels = []
        bug_data   = []
        for bug in bugs:
            upvotes = bug.upvotes.count()
            label = bug.get_short()
            bug_data.append(upvotes)
            bug_labels.append(label)


        feature_labels = []
        feature_data   = []
        for feat in features:
            upvotes = feat.upvotes.count()
            label = feat.get_short()
            feature_data.append(upvotes)
            feature_labels.append(label)

        data = {
            "bugs": {
                "labels":  bug_labels,
                "datasets": [{
                  "data": bug_data,
                  "throughputs": [{
                      "month1": [{"fixperday": 8,
                                  "fixperweek": 16,
                                  "fixpermonth": 19}],
                      "month2": [{"fixperday": 8,
                                  "fixperweek": 16,
                                  "fixpermonth": 19}],
                      "month3": [{"fixperday": 8,
                                  "fixperweek": 16,
                                  "fixpermonth": 19}],
                      "month4": [{"fixperday": 8,
                                  "fixperweek": 16,
                                  "fixpermonth": 19}],
                      "month5": [{"fixperday": 8,
                                  "fixperweek": 16,
                                  "fixpermonth": 19}],
                      "month6": [{"fixperday": 8,
                                  "fixperweek": 16,
                                  "fixpermonth": 19}]
                  }]
                }]
            },
            "features": {
                "labels":  feature_labels,
                "datasets": [{
                  "data": feature_data
                }]
            }
        }
        return Response(data)



class PostListView(ListView):
    """ Class ListView to display posts from homepage"""
    model = Post
    template_name = 'tracker/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 7



class UserPostListView(ListView):
    """ Class ListView to show list of posts for a particular user"""
    model = Post
    template_name = 'tracker/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 6

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



def graphs(request):
    return render(request, 'tracker/graphs.html', {'title':'Graphs'})



class PostLikeToggle(LoginRequiredMixin, RedirectView):
    """ Class Redirect View for upvoting a Bug / Feature
    Along with the authentication check the code also checks that
    a user has purchased an upvote plan if they they want to upvote a feature request
    """

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, id=self.kwargs.get('pk'))
        url_ = post.get_absolute_url()
        user = self.request.user
        if user.is_authenticated and post.ticket_type == 'BG':
            if user in post.upvotes.all():
                post.upvotes.remove(user)
            else:
                post.upvotes.add(user)
        elif user.is_authenticated and post.ticket_type == 'FT':
            if user.profile.purchased.name:
                if user in post.upvotes.all():
                    post.upvotes.remove(user)
                else:
                    post.upvotes.add(user)
            messages.warning(self.request, f'Your have not yet purchased upvotes')
        return url_



class PostCreateView(LoginRequiredMixin, CreateView):
    """ Class CreateView to create new post"""
    model = Post
    fields = ['title', 'content', 'ticket_type']

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
    fields = ['title', 'content', 'ticket_type']

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
