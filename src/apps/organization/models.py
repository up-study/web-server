from django.db import models
import uuid

from src.apps.users.models import User


class Organization(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    owner = models.ForeignKey(
        User, related_name="owner", on_delete=models.CASCADE, null=True
    )
    members = models.ManyToManyField(
        User, related_name="members", through="OrganizationMember"
    )


class OrganizationMember(models.Model):
    ORGANIZATION_ROLS = [
        ("1", "Member"),
        ("2", "Writer"),
        ("3", "Teacher"),
        ("4", "Reviewer"),
        ("5", "Support"),
        ("6", "Manager"),
        ("7", "Co Owner"),
        ("8", "Owner"),
    ]
    private = models.BooleanField(default=True)
    role = models.CharField(max_length=1, choices=ORGANIZATION_ROLS, default="Member")
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="organization"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
