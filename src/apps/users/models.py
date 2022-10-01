from django.db import models

from django.contrib.auth.models import AbstractUser

from src.apps.users.consts import Role
# from src.apps.achievements.models import Achievement


class User(AbstractUser):
    role = models.PositiveSmallIntegerField(
        choices=Role.choices, verbose_name='Role',
        default=Role.STUDENT
    )
    github_link = models.URLField(verbose_name='GitHub Profile', null=True, blank=True)
    # achievements = models.ManyToManyField(Achievement)
    # TODO: probably will be moved to Student Profile model

    def __str__(self):
        return self.username
