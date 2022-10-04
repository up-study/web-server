from django_filters import rest_framework as filter
from src.apps.resume.models import Resume


class ResumeFilter(filter.FilterSet):
    class Meta:
        model = Resume
        fields = (
            "programming_language__name",
            "language__name",
            "programming_language__code",
            "language__code",
        )
