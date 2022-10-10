from django_filters import FilterSet, CharFilter
from src.apps.resume.models import Resume


class ResumeFilter(FilterSet):
    programming_language = CharFilter(
        "programming_language__name", lookup_expr="startswith"
    )
    language = CharFilter("language__name", lookup_expr="startswith")
    programming_language_code = CharFilter(
        "programming_language__code", lookup_expr="startswith"
    )
    language_code = CharFilter("language__code", lookup_expr="startswith")
    city = CharFilter("city__name", lookup_expr="startswith")
    country = CharFilter("city__country__name", lookup_expr="startswith")

    class Meta:
        model = Resume
        fields = (
            "programming_language",
            "programming_language_code",
            "language",
            "language_code",
            "city",
            "country",
        )
