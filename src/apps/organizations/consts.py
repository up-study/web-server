from django.db import models


class OrganizationRoles(models.IntegerChoices):
    MEMBER = 1, "Member"
    WRITER = 2, "Writer"
    TEACHER = 3, "Teacher"
    REVIEWER = 4, "Reviewer"
    SUPPORT = 5, "Support"
    MANAGER = 6, "Manager"
    CO_OWNER = 7, "Co Owner"
    OWNER = 8, "Owner"
