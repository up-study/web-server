from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from src.apps.resume.models import Resume
from src.apps.resume.api.serializers import ResumeSerializer
from src.apps.resume.api.filters import ResumeFilter


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = ResumeFilter
    search_fields = (
        "language__name",
        "language__code",
        "programming_language__code",
        "programming_language__code",
        "city__name",
    )
