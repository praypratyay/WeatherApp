from django.shortcuts import render
from .utils import get_qualitative_name
from .config import OPEN_WEATHER_API_KEY

from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CityWeather, AirQuality

import requests

class WeatherAPIView(APIView):
    def get(self, request, city_name):
        # Fetch current weather data from OpenWeatherMap API
        try:
            weather_api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPEN_WEATHER_API_KEY}&units=metric'
            weather_data = requests.get(weather_api_url).json()

            # Store weather data in the database
            CityWeather.objects.create(
                city_name=city_name,
                temperature=weather_data['main']['temp'],
                humidity=weather_data['main']['humidity'],
                wind_speed=weather_data['wind']['speed'],
            )

            return Response(weather_data)
        except Exception as e:
            # Handle exceptions, log them, and return an appropriate error response
            raise APIException(detail="Error in processing the request from weatherAPI for this cityname.")

class AirQualityAPIView(APIView):
    def get(self, request,lat,lon):
        # Fetch air quality data from OpenWeatherMap Air Pollution API
        try:
            air_quality_api_url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={OPEN_WEATHER_API_KEY}'
            air_quality_data = requests.get(air_quality_api_url).json()['list'][0]

            # Store air quality data in the database
            AirQuality.objects.create(
                lat=lat,
                lon=lon,
                aqi=air_quality_data['main']['aqi'],
                so2=air_quality_data['components']['so2'],
                no2=air_quality_data['components']['no2'],
                pm10=air_quality_data['components']['pm10'],
                pm25=air_quality_data['components']['pm2_5'],
                o3=air_quality_data['components']['o3'],
                co=air_quality_data['components']['co'],
            )

            # Adding qualitative names
            qNames = {}
            for pollutant in air_quality_data['components']:
                qNames[pollutant] = get_qualitative_name(pollutant,air_quality_data['components'][pollutant])

            air_quality_data["QualitativeNames"] = qNames

            return Response(air_quality_data)
        
        except Exception as e:
            # Handle exceptions, log them, and return an appropriate error response
            raise APIException(detail="Error in processing the request from AirPollutionAPI for these coordinates.")

    
class CombinedAPIView(APIView):
    def get(self, request, city_name):
        try:
            # Call WeatherAPIView to fetch weather data
            weather_response = WeatherAPIView().get(request, city_name)

            # Call AirQualityAPIView to fetch air quality data
            air_quality_response = AirQualityAPIView().get(request, lat=weather_response.data['coord']['lat'], lon=weather_response.data['coord']['lon'])

            # Combine weather and air quality data in the response
            response_data = {
                'weather': weather_response.data,
                'air_quality': air_quality_response.data,
            }
            return Response(response_data)

        except Exception as e:
            # Handle exceptions, log them, and return an appropriate error response
            raise APIException(detail="Error in processing the combinedrequest using both views.")