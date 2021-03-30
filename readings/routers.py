from rest_framework.routers import SimpleRouter
from .viewsets import CoordinatesViewSet, VibrationViewSet


api_routes = SimpleRouter()
api_routes.register("coordinates", CoordinatesViewSet, base_name="coordinates-api")
api_routes.register("vibrations", VibrationViewSet, base_name="vibrations-api")

api_router = api_routes.urls

url_patterns = api_router

