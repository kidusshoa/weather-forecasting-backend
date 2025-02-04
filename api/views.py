from rest_framework import viewsets
from .models import WeatherPrediction
from .serializers import WeatherPredictionSerializer

class WeatherPredictionViewSet(viewsets.ModelViewSet):
    queryset = WeatherPrediction.objects.all()
    serializer_class = WeatherPredictionSerializer
