from rest_framework import viewsets, filters
from django_filters import rest_framework as filter

from src.apps.resume.models import Resume
from src.apps.resume.api.serialezers import ResumeSerializer
from src.apps.resume.api.filters import ResumeFilter


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    filter_backends = (filter.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = ResumeFilter
    search_fields = (
        "language__name",
        "language__code",
        "programming_language__code",
        "programming_language__code",
    )
