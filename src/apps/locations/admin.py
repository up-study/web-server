from django.contrib import admin

from src.apps.locations.models import Country, City


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass
