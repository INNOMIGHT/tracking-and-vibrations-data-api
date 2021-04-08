from django.db.models import (
    CharField,
    Model,
)
from django_extensions.db.fields import AutoSlugField


class Coordinates(Model):

    gps_coordinates = CharField(max_length=31)
    slug = AutoSlugField(max_length=31, populate_from=["gps_coordinates"])

    class Meta:
        ordering = ["gps_coordinates"]


class Vibrations(Model):

    vibration_reading = CharField(max_length=31)
    slug = AutoSlugField(max_length=31, populate_from=["vibration_reading"])

    class Meta:
        ordering = ["vibration_reading"]


class Sensors(Model):

    location = CharField(max_length=31)
    slug = AutoSlugField(max_length=31, populate_from=["location"])

    class Meta:
        ordering = ["location"]






