from django.contrib import admin

from src.apps.achievements.models import Achievement


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    pass
