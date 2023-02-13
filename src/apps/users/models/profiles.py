from django.db import models
from django.db.models import Q


class Profile(models.Model):
    user = models.OneToOneField(
        "users.User", null=True, blank=True, on_delete=models.CASCADE
    )
    organization = models.OneToOneField(
        "organizations.Organization", null=True, blank=True, on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=(
                    Q(user__isnull=True, organization__isnull=False)
                    | Q(user__isnull=False, organization__isnull=True)
                ),
                name="profile_user_organization_constraint",
            )
        ]
