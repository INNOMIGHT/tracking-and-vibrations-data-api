from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Coordinates, Vibrations


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
