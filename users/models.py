import stripe
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.contrib.auth.models import User
from products.models import Product
from PIL import Image

stripe.api_key = settings.STRIPE_SECRET_KEY

class Profile(models.Model):
    """User profile details model """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(Product, blank=True)
    stripe_id = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        """Inherit User.save function and add the Pillow functions before save """
        super(Profile, self).save(*args, **kwargs)
        """Pass user image into Pillow library and resize image """
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    
