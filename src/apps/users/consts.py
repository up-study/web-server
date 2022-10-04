from django.db import models


class UserType(models.IntegerChoices):
    STUDENT = 1, "Student"
    COACH = 2, "Coach"
