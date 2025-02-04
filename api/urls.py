from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WeatherPredictionViewSet

router = DefaultRouter()
router.register(r'predictions', WeatherPredictionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
