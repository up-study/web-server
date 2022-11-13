from rest_framework import serializers

from src.apps.courses.models import Section, Course
from src.apps.base.models import Image

from src.apps.resume.models import ProgramminngLanguage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("id", "photo")


class ProgrammingLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramminngLanguage
        fields = ("id", "name", "code")


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ("id", "name", "description")


class CourseSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    programming_languages = ProgrammingLanguagesSerializer(many=True)
    section = SectionSerializer(many=True)

    class Meta:
        model = Course
        fields = (
            "id",
            "name",
            "description",
            "published",
            "images",
            "section",
            "programming_languages",
        )
