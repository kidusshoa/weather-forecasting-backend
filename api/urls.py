from django.urls import path
from .views import predict_weather  

urlpatterns = [
    path('predict/', predict_weather),  
]
