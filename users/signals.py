import stripe

from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile



stripe.api_key = settings.STRIPE_SECRET_KEY


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Signal to automatically create a user profile when a user is created """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """Signal to save a user profile """
    instance.profile.save()

# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     """Signal to save a user profile """
#     user_profile, created = Profile.objects.get_or_create(user=instance)
#
#     if user_profile.stripe_id is None or user_profile.stripe_id == '':
#         new_stripe_id = stripe.Customer.create(email=instance.email)
#         user_profile.stripe_id = new_stripe_id['id']
#         user_profile.save()

# post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)
