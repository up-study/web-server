from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import uuid

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from src.apps.users.consts import UserType
from src.apps.base.models import Image


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    email_notifications = models.BooleanField(default=False)
    wa_notifications = models.BooleanField(default=False)
    tg_notifications = models.BooleanField(default=False)
    profile_photo = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    email = models.EmailField(_("email address"), null=True)
    phone = PhoneNumberField(null=True)

    type = models.PositiveSmallIntegerField(
        choices=UserType.choices, verbose_name="User Type", default=UserType.STUDENT
    )
    github_link = models.URLField(verbose_name="GitHub Profile", null=True, blank=True)
    followers = models.ManyToManyField(
        "self", related_name="following", blank=True, symmetrical=False
    )

    REQUIRED_FIELDS = ["first_name", "last_name", "email"]

    def __str__(self):
        return self.username

    @property
    def followers_amount(self):
        return self.followers.count()

    @property
    def following_amount(self):
        return self.following.count()

    class Meta:
        unique_together = ("email", "type")
