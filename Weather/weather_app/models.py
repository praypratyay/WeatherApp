from django.db import models

class CityWeather(models.Model):
    city_name = models.CharField(max_length=255)
    temperature = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()

class AirQuality(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    aqi = models.IntegerField()
    so2 = models.FloatField()
    no2 = models.FloatField()
    pm10 = models.FloatField()
    pm25 = models.FloatField()
    o3 = models.FloatField()
    co = models.FloatField()