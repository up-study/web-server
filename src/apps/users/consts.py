from django.db import models


class Role(models.IntegerChoices):
    STUDENT = 1, 'Student'
    COACH = 2, 'Coach'
    MANAGER = 3, 'Manager'
