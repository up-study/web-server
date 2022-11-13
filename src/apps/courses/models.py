from django.db import models

from src.apps.resume.models import ProgramminngLanguage
from src.apps.base.models import Image


class Section(models.Model):
    name = models.CharField(max_length=200, verbose_name="Section Name")
    # lesson_group = models.ManyToManyField(LessonGroup)
    description = models.TextField(verbose_name="Section Description")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Section"


class Course(models.Model):
    name = models.CharField(max_length=200, verbose_name="Course Name")
    description = models.TextField(verbose_name="Course Description")
    published = models.BooleanField()
    images = models.ManyToManyField(Image)
    section = models.ManyToManyField(Section)
    programming_languages = models.ManyToManyField(ProgramminngLanguage)

    def __str__(self):
        return self.name
