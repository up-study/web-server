import pytest
from django.db.utils import IntegrityError

from src.apps.base.tests import baker
from src.apps.users.models.profiles import Profile


@pytest.mark.django_db
def test_profile_creation_constraints() -> None:
    user = baker.make_recipe("users.user")
    organization = baker.make_recipe("users.organization")

    # Check that the organization property is set correctly
    profile = Profile.objects.create(organization=organization)
    assert profile.organization == organization

    # Check that the user property is set correctly
    profile = Profile.objects.create(user=user)
    assert profile.user == user

    # Check that creating a profile with user and organization causes IntegrityError
    with pytest.raises(IntegrityError):
        Profile.objects.create(user=user, organization=organization)
