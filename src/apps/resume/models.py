from django.db import models


class ProgramminngLanguage(models.Model):
    name = models.CharField(
        max_length=120, verbose_name="Name of the Programming Language"
    )
    code = models.CharField(
        max_length=120, verbose_name="Name Code"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Programming Language'


class Language(models.Model):
    name = models.CharField(
        max_length=120, verbose_name="Language"
    )
    code = models.CharField(
        max_length=120, verbose_name="Name Code"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Language'


class Country(models.Model):
    name = models.CharField(
        max_length=170, verbose_name="Country Name"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Country"


class City(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="City Name"
    )
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, verbose_name="Country",
        related_name='city'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "City"


class Resume(models.Model):
    # user = models.ForeignKey(
    #     'users.User', on_delete=models.CASCADE,
    #     verbose_name='User'
    # )
    first_name = models.CharField(
        max_length=120, verbose_name="First Name"
    )
    last_name = models.CharField(
        max_length=120, verbose_name="Last Name"
    )
    about_me = models.TextField(
        verbose_name="About Me"
    )
    programming_language = models.ManyToManyField(
        ProgramminngLanguage
    )
    language = models.ManyToManyField(
        Language
    )
    # TODO perhaps a study program will be added

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Resume'
