from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from src.apps.users.api.views import UserViewSet
from src.apps.resume.api.views import ResumeViewSet


router = SimpleRouter()
router.register("users", UserViewSet)
router.register("resume", ResumeViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api/v1/", include("src.apps.api_auth.api.urls")),
]
