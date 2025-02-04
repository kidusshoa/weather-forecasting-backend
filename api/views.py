from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import joblib
import os

# Load the model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'weather_model.pkl')
model = joblib.load(model_path)

@api_view(['POST'])
def predict_weather(request):
    try:
        data = request.data
        print("Received Data:", data)  # ✅ Log incoming data

        required_fields = ['temperature', 'humidity', 'wind_speed', 'pressure_mb', 'cloud', 'air_quality_PM2_5']
        missing_fields = [field for field in required_fields if field not in data]

        if missing_fields:
            return Response({'error': f'Missing fields: {missing_fields}'}, status=status.HTTP_400_BAD_REQUEST)

        features = [
            float(data['temperature']),
            float(data['humidity']),
            float(data['wind_speed']),
            float(data['pressure_mb']),
            float(data['cloud']),
            float(data['air_quality_PM2_5'])
        ]

        prediction = model.predict([features])
        return Response({'predicted_precipitation': prediction[0]}, status=status.HTTP_200_OK)

    except ValueError as ve:
        return Response({'error': f'Invalid input: {str(ve)}'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
