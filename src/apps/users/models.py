from django.db import models

from django.contrib.auth.models import AbstractUser

from apps.users.consts import Role


class User(AbstractUser):
    role = models.PositiveSmallIntegerField(
        choices=Role.choices, verbose_name='Role',
        default=Role.STUDENT
    )
    github_link = models.CharField(
        max_length=120, verbose_name='GitHub Profile'
    )

    def __str__(self):
        return self.username
