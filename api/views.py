from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
import requests
import json
import geocoder
from ipware import get_client_ip



def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={settings.OPENWEATHERMAP_API_KEY}'
    response = requests.get(url)
    return response.json()


def help(request):
    visitor_name = request.GET.get('visitor_name', 'Guest')

    client_ip, is_routable = get_client_ip(request)

    ip_address = client_ip

    url = f"http://ipinfo.io/{ip_address}?token=84476190df868e"
    response = requests.get(url)
    res = response.json()

    city = res['city']

    # Get weather data
    weather_data = get_weather(city)
    temperature = weather_data['main'].get('temp', 'N/A')

    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {city}"

    response = {
        "client_ip": ip_address,
        "location": city,
        "greeting": greeting
    }

    return JsonResponse(response)