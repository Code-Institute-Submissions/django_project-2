from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostLikeToggle,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    CommentCreateView,
    ChartData)
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='tracker-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/upvote', PostLikeToggle.as_view(), name='post-upvote'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='comment-create'),
    path('graphs/', views.graphs, name='tracker-graphs'),
    path('api/charts/data', ChartData.as_view()),
    path('about/', views.about, name='tracker-about'),
]
