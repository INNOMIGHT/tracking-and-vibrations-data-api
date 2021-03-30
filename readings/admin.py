from django.contrib import admin
from .models import Coordinates, Vibrations


@admin.register(Coordinates)
class CoordinatesAdmin(admin.ModelAdmin):
    list_display = ("gps_coordinates", "slug")


@admin.register(Vibrations)
class VibrationsAdmin(admin.ModelAdmin):
    list_display = ("vibration_reading", "slug")
