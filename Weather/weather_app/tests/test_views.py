from django.test import TestCase, Client
from rest_framework import status
from django.urls import reverse

class WeatherAPITest(TestCase):
    def test_get_weather_data(self):
        client = Client()

        response = client.get(reverse('weather_api', kwargs={"city_name":'London'}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('main', response.json())
        self.assertIn('wind', response.json())
        self.assertIn('name', response.json())  

    def test_invalid_city_name(self):
        client = Client()

        response = client.get(reverse('weather_api', kwargs={"city_name":'INVALID'}))

        self.assertIn('detail', response.json())  

class AirQualityAPITest(TestCase):
    def test_get_air_quality_data(self):
        client = Client()

        response = client.get(reverse('air_quality_api', kwargs={"lat":'55',"lon":'24'}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('main', response.json())
        self.assertIn('components', response.json())
        self.assertIn('QualitativeNames', response.json())

    def test_invalid_coordinates(self):
        client = Client()

        response = client.get(reverse('air_quality_api', kwargs={"lat":'INVALID',"lon":'INVALID'}))

        self.assertIn('detail', response.json())

class CombinedAPITest(TestCase):
    def test_combined_data(self):
        client = Client()

        response = client.get(reverse('combined_api', kwargs={"city_name":'London'}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('weather', response.json())
        self.assertIn('air_quality', response.json())

    def test_invalid_city_name(self):
        client = Client()

        response = client.get(reverse('combined_api', kwargs={"city_name":'INVALID'}))

        self.assertIn('detail', response.json())  

# Test command 
# python3 .\manage.py test weather_app.tests