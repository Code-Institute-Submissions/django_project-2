from django.test import TestCase

from users.models import User
from .models import Post, Comment


class PostTest(TestCase):
    def setUp(self):
        """Create a user and a post"""
        user1 = User.objects.create(username='kenny', password='wavejumper')
        post1 = Post.objects.create(title="heroku bug title", content="always problems with heroku", ticket_type="BG", status="TD", author=user1)

    def test_get_short(self):
        """Test the shorten post title function"""
        user1 = User.objects.create(username='drexciya', password='wavejumper')
        post1 = Post.objects.create(title="no midi in 808", content="Need to get a midi mod for 808", ticket_type="BG", status="TD", author=user1)
        self.assertEqual(post1.get_short(), 'no midi in')

    def test_get_comment_total(self):
        """Test the number of post comments"""
        user2 = User.objects.create(username='carlcraig', password='wavejumper')
        post2 = Post.objects.create(title="no midi in 808", content="Need to get a midi mod for 808",
                                    ticket_type="BG", status="TD", author=user2)
        comment1 = Comment.objects.create(text='this is a comment', author=user2, post=post2)
        self.assertEqual(post2.get_comment_total(), 1)

    def test_get_upvotes_total(self):
        """Test the number of post upvotes"""
        user3 = User.objects.create(username='dancurtin', password='wavejumper')
        post3 = Post.objects.create(title="no midi in 808", content="Need to get a midi mod for 808",
                                    ticket_type="BG", status="TD", author=user3)
        self.assertEqual(post3.get_upvotes_total(), 0)

    def test_like_state(self):
        """Test the number of post upvotes"""
        user4 = User.objects.create(username='moodymann', password='wavejumper')
        user5 = User.objects.create(username='omars', password='wavejumper')
        post5 = Post.objects.create(title="no midi in 808", content="Need to get a midi mod for 808",
                                    ticket_type="BG", status="TD", author=user5)
        post6 = Post.objects.create(title="MPC X update", content="Need to install updates",
                                    ticket_type="BG", status="TD", author=user5)
        post5.upvotes.add(user4)
        self.assertEqual(len(post5.like_state()), 1)
        self.assertEqual(len(post6.like_state()), 0)
