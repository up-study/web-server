from django.contrib import admin

from src.apps.courses.models import Course, Section


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAmdin(admin.ModelAdmin):
    pass
