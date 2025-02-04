from django.db import models

class WeatherPrediction(models.Model):
    date = models.DateField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    precipitation = models.FloatField()
    wind_speed = models.FloatField()

    def __str__(self):
        return f"Weather on {self.date}"
