from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from src.apps.users.api.views import UserViewSet
from src.apps.resume.api.views import ResumeViewSet
from src.apps.courses.api.views import CourseViewSet


router = SimpleRouter()
router.register("users", UserViewSet)
router.register("resume", ResumeViewSet)
router.register("courses", CourseViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api/v1/", include("src.apps.base.api.urls")),
    path("api/v1/", include("src.apps.api_auth.api.urls")),
]
