from django.contrib import admin

from src.apps.resume.models import (
    Language, Resume, ProgramminngLanguage
)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(ProgramminngLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    pass
