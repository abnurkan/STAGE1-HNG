from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
import requests
import json





def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={settings.OPENWEATHERMAP_API_KEY}'
    response = requests.get(url)
    return response.json()


def myapi(request):
    visitor_name = request.GET.get('visitor_name', 'Guest')
    client_ip = request.META.get('REMOTE_ADDR')

    ip=requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    res =requests.get('http://ip-api.com/json/'+ip_data["ip"])

    location_data_one=res.text
    location_data = json.loads(location_data_one)


    # Get geolocation data
    
    city = location_data['city']

    # Get weather data
    weather_data = get_weather(city)
    temperature = weather_data['main'].get('temp', 'N/A')

    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {city}"

    response = {
        "client_ip": client_ip,
        "location": city,
        "greeting": greeting
    }

    return JsonResponse(response)