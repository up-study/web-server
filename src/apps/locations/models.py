from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=200, verbose_name="Country Name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Country"


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name="City Name")
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="cities"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "City"
