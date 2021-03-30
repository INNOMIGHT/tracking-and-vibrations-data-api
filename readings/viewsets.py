from rest_framework.viewsets import ModelViewSet
from .models import Coordinates, Vibrations
from .serializer import CoordinateSerializer, VibrationSerializer


class CoordinatesViewSet(ModelViewSet):

    queryset = Coordinates.objects.all()
    serializer_class = CoordinateSerializer
    lookup_field = "slug"


class VibrationViewSet(ModelViewSet):

    queryset = Vibrations.objects.all()
    serializer_class = VibrationSerializer
    lookup_field = "slug"

