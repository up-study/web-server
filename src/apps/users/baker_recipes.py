from model_bakery.recipe import Recipe

from src.apps.users.models import User
from src.apps.organizations.models import Organization


user = Recipe(User)
organization = Recipe(Organization)
