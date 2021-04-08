from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Coordinates, Vibrations, Sensors


class CoordinateSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Coordinates
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "coordinates-api-detail"
            }
        }


class VibrationSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Vibrations
        fields = "__all__"
        extra_kwargs = {
            "url": {
                "lookup_field": "slug",
                "view_name": "vibrations-api-detail"
            }
        }


class SensorSerializer(HyperlinkedModelSerializer):

    model = Sensors
    fields = "__all__"
    extra_kwargs = {
        "url": {
            "loopkup_field": "slug",
            "view_name": "sensors-api-detail"
        }
    }
