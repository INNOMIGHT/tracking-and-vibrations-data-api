from rest_framework.routers import SimpleRouter
from .viewsets import CoordinatesViewSet, VibrationViewSet, SensorsViewSet


api_routes = SimpleRouter()
api_routes.register("coordinates", CoordinatesViewSet, basename="coordinates-api")
api_routes.register("vibrations", VibrationViewSet, basename="vibrations-api")
api_routes.register("sensors", SensorsViewSet, basename="sensors-api")

api_router = api_routes.urls

url_patterns = api_router

