from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
import json
import requests
from django.http import JsonResponse


def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={settings.OPENWEATHERMAP_API_KEY}'
    response = requests.get(url)
    return response.json()

def help(request):
    visitor_name = request.GET.get('visitor_name')
    # Get user IP address
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    try:
        response = requests.get(f'http://ipinfo.io/{ip}?token=84476190df868e')
        location_data = response.json()
        city = location_data.get('city', 'Unknown')
    except Exception as e:
        city = "Unknown"
        country = "Unknown"

    
    # Get weather data
    weather_data = get_weather(city)
    temperature = weather_data['main'].get('temp', 'N/A')
    
    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {city}"
   
    response = {
        'client_ip': ip,
        'city': city,
        'greeting': greeting
    }
    return JsonResponse(response)
