from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    """User profile details model """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        """Inherit User.save function and add the Pillow functions before save """
        super().save()
        """Pass user image into Pillow library and resize image """
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
