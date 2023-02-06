from django.db import models
import uuid

from src.apps.users.models import User


class Organization(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    owner = models.ForeignKey(
        User, related_name="owners", on_delete=models.CASCADE, null=True
    )
    members = models.ManyToManyField(
        User, related_name="organizations", through="OrganizationMember"
    )


class OrganizationRoles(models.IntegerChoices):
    MEMBER = 1, "Member"
    WRITER = 2, "Writer"
    TEACHER = 3, "Teacher"
    REVIEWER = 4, "Reviewer"
    SUPPORT = 5, "Support"
    MANAGER = 6, "Manager"
    CO_OWNER = 7, "Co Owner"
    OWNER = 8, "Owner"


class OrganizationMember(models.Model):
    private = models.BooleanField(default=True)
    role = models.IntegerField(
        choices=ORGANIZATION_ROLS.choices, default=ORGANIZATION_ROLS.MEMBER
    )
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="organizations"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
