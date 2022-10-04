from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from src.apps.users.consts import UserType
from src.apps.achievements.models import Achievement


class User(AbstractUser):
    email = models.EmailField(_("email address"), null=True)
    phone = models.CharField(_("phone number"), max_length=32, null=True)

    type = models.PositiveSmallIntegerField(
        choices=UserType.choices, verbose_name="User Type", default=UserType.STUDENT
    )
    github_link = models.URLField(verbose_name="GitHub Profile", null=True, blank=True)

    REQUIRED_FIELDS = ["first_name", "last_name", "email"]

    def __str__(self):
        return self.username

    class Meta:
        unique_together = ("email", "type")


class StudentProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="student_profile"
    )
    achievements = models.ManyToManyField(Achievement)


class CoachProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="coach_profile"
    )
