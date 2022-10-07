from rest_framework import serializers

from src.apps.resume.models import Language, ProgramminngLanguage, Resume
from src.apps.locations.models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "name")


class ProgrammingLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramminngLanguage
        fields = ("id", "name", "code")


class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ("id", "name", "code")


class ResumeSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    language = LanguagesSerializer(many=True)
    programming_language = ProgrammingLanguagesSerializer(many=True)

    class Meta:
        model = Resume
        fields = (
            "id",
            "first_name",
            "last_name",
            "about_me",
            "language",
            "programming_language",
            "city",
        )
