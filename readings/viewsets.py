from rest_framework.viewsets import ModelViewSet
from .models import Coordinates, Vibrations, Sensors
from .serializer import CoordinateSerializer, VibrationSerializer, SensorSerializer


class CoordinatesViewSet(ModelViewSet):

    queryset = Coordinates.objects.all()
    serializer_class = CoordinateSerializer
    lookup_field = "slug"


class VibrationViewSet(ModelViewSet):

    queryset = Vibrations.objects.all()
    serializer_class = VibrationSerializer
    lookup_field = "slug"
    

class SensorsViewSet(ModelViewSet):

    queryset = Sensors.objects.all()
    serializer_class = SensorSerializer
    lookup_field = "slug"

