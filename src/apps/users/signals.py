from django.db.models.signals import post_save
from django.dispatch import receiver

from src.apps.users.consts import UserType
from src.apps.users.models import (
    CoachProfile, StudentProfile, User
)


@receiver(post_save, sender=User)
def create_profile(created, instance, **_):
    if created:
        if instance.type == UserType.STUDENT:
            StudentProfile.objects.create(user=instance)
        elif instance.type == UserType.COACH:
            CoachProfile.objects.create(user=instance)
