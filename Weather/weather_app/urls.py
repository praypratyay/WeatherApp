from django.urls import path
from .views import WeatherAPIView, AirQualityAPIView,CombinedAPIView

urlpatterns = [
    path('weather/<str:city_name>/', WeatherAPIView.as_view(), name='weather_api'),
    path('air-quality/<str:lat>/<str:lon>/', AirQualityAPIView.as_view(), name='air_quality_api'),
    path('<str:city_name>/', CombinedAPIView.as_view(), name='combined_api'),
]