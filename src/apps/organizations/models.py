from django.db import models
import uuid

from src.apps.users.models.users import User
from src.apps.organizations.consts import OrganizationRoles


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


class OrganizationMember(models.Model):
    private = models.BooleanField(default=True)
    role = models.IntegerField(
        choices=OrganizationRoles.choices, default=OrganizationRoles.MEMBER
    )
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="organizations"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
