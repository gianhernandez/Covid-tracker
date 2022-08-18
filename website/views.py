from django.shortcuts import render
import requests
from datetime import datetime
from decouple import config


# Create your views here.
def index(request):
    # API Info
    url = 'https://covid-193.p.rapidapi.com/statistics?country=all'
    statistics = "https://covid-193.p.rapidapi.com/statistics"

    headers = {
        "X-RapidAPI-Key": config('RAPID_API_KEY'),
        "X-RapidAPI-Host": "covid-193.p.rapidapi.com"
    }

    # API requests
    response = requests.request("GET", statistics, headers=headers).json()
    countries = requests.request("GET", url, headers=headers).json()

    all_countries = countries['response']

    # World Covid statistics
    world_total_deaths = countries['response'][0]['deaths']['total']
    world_new_deaths = countries['response'][0]['deaths']['new']
    world_new_cases = countries['response'][0]['cases']['new']
    world_total_cases = countries['response'][0]['cases']['total']
    world_new_recovered = countries['response'][0]['cases']['recovered']
    world_total_recovered = countries['response'][0]['cases']['recovered']

    # Country List
    country = []
    total_deaths = []

    total_info = response['response']

    # Loop to separate the countries statistics
    for x in total_info:
        country.append(x['country'])
        total_deaths.append(x['deaths']['total'])

    # Displaying actual year
    now = datetime.now()
    year = now.year

    return render(request, 'index.html', {'total_deaths': total_deaths,
                                          'total_info': total_info,
                                          'all_countries': all_countries,
                                          'world_new_cases': world_new_cases,
                                          'world_total_cases': world_total_cases,
                                          'world_new_recovered': world_new_recovered,
                                          'world_total_recovered': world_total_recovered,
                                          'world_new_deaths': world_new_deaths,
                                          'world_total_deaths': world_total_deaths,
                                          'year': year
                                          })
