from rest_framework.viewsets import ModelViewSet

from src.apps.courses.api.serializers import CourseSerializer
from src.apps.courses.models import Course


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
