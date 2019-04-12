from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    """ Tracker Post model"""
    BUG = 'BG'
    FEATURE = 'FT'
    TICKET_CHOICES = (
        (BUG, 'Bug'),
        (FEATURE, 'Feature'),
    )

    REQUESTED = 'RQ'
    TODO = 'TD'
    FIXED = 'FX'
    STATUS_CHOICES = (
        (REQUESTED, 'Requested'),
        (TODO, 'Todo'),
        (FIXED, 'Fixed'),
    )

    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    ticket_type = models.CharField(
        max_length=2,
        choices=TICKET_CHOICES,
        default=BUG,
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=TODO,
    )
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    upvotes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_short(self):
        return self.title[:10]

    def get_comment_total(self):
        """ Get comment count for sending to template"""
        return self.comments.count()

    def get_upvotes_total(self):
        """ Count number of likes in post object """
        return self.upvotes.count()

    def like_state(self):
        """ Function to help determine if user is in likes list """
        return self.upvotes.all()

    def inc_view_count(self):
        """ Function to increase view count when a user views a post """
        self.views += 1

    def get_upvote_url(self):
        """ Send post path string to view"""
        return reverse('post-upvote', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        """ Send post path string to view"""
        return reverse('post-detail', kwargs={'pk': self.pk})



class Comment(models.Model):
    """ User comments model"""
    text = models.CharField(max_length=800)
    created_date = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """ Dunder method to improve birds eye view of comments in Django Admin"""
        if len(self.text) > 14:
            return f'{self.text[:14]}...'
        else:
            return f'{self.text}'

    def get_absolute_url(self):
        """ Send post path string to view for redirecting user back to post view"""
        return reverse('post-detail', kwargs={'pk': self.post.pk})
