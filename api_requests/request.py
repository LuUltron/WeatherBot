"""
согласно PEP 8 импорты необходимо располагать:
1 импорты из стандартной библиотеки
2 импорты сторонних библиотек
3 импорты модулей текущего проекта
Вставляйте пустую строку между каждой группой импортов.
"""
import json 

import requests

from settings import config

def get_city_coord(city):
    payload = {'geocode': city, 'apikey': config.geo_key, 'format': 'json'}
    r = requests.get('https://geocode-maps.yandex.ru/1.x', params=payload)
    geo = json.loads(r.text)
    return geo['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']


#print(get_city_coord('Калиниград'))

def get_weather(city):
    coordinates = get_city_coord(city).split()
    payload = {'lat': coordinates[1], 'lon': coordinates[0], 'lang': 'ru_RU'}
    r = requests.get('https://api.weather.yandex.ru/v2/forecast', params=payload, headers=config.weather_key)
    weather_data = json.loads(r.text)
    return weather_data['fact']

#print(get_weather('Калиниград'))