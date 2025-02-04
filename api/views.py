import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import joblib


model = joblib.load('api/weather_model.pkl')

def geocode_city(city):
    username = 'kidusshoa'
    url = f'http://api.geonames.org/searchJSON?q={city}&maxRows=1&username={username}'
    print(f"Requesting GeoNames API: {url}")  
    response = requests.get(url)

    print(f"Response Status: {response.status_code}") 
    print(f"Response Data: {response.text}")  

    if response.status_code == 200:
        data = response.json()
        if data['geonames']:
            return float(data['geonames'][0]['lat']), float(data['geonames'][0]['lng'])
    return None, None


@api_view(['POST'])
def predict_weather(request):
    data = request.data
    city = data.get('city')

    if city:
        latitude, longitude = geocode_city(city)
        if latitude is None:
            return Response({'error': 'City not found'}, status=status.HTTP_400_BAD_REQUEST)
        data['latitude'], data['longitude'] = latitude, longitude

    required_fields = ['temperature', 'humidity', 'wind_speed', 'pressure_mb', 'cloud', 'air_quality_PM2_5']
    if not all(field in data for field in required_fields):
        return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

    features = [
        float(data['temperature']),
        float(data['humidity']),
        float(data['wind_speed']),
        float(data['pressure_mb']),
        float(data['cloud']),
        float(data['air_quality_PM2_5'])
    ]

    prediction = model.predict([features])
    return Response({'predicted_precipitation': prediction[0]})
