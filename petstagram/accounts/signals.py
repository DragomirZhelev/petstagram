from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from petstagram.accounts.utils import send_welcome_email

from petstagram.accounts.models import Profile

UserModel = get_user_model()

@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

        send_welcome_email(
            email=instance.email,
            username=instance.email,
        )