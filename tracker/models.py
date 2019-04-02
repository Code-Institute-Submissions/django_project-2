from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    """ Tracker Post model"""
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    todo = models.BooleanField(default=True)
    fixed = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_comment_total(self):
        """ Get comment count for sending to template"""
        return self.comments.count()

    def get_absolute_url(self):
        """ Send post path string to view"""
        return reverse('post-detail', kwargs={'pk': self.pk})



class Comment(models.Model):
    """ User comments model"""
    text = models.CharField(max_length=320)
    created_date = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        """ Dunder method to improve birds eye view of comments in Django Admin"""
        if len(self.text) > 14:
            return f'{self.text[:14]}...'
        else:
            return f'{self.text}'

    def get_absolute_url(self):
        """ Send post path string to view for redirecting user back to post view"""
        return reverse('post-detail', kwargs={'pk': self.post.pk})
