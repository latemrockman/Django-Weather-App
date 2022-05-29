import requests
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm

from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.

def sort_info_by_temp(all_cities):
    n = 0
    index_list = []
    for i in all_cities:
        temp = i['temp']
        index_list.append((temp, n))
        n += 1

    index_list.sort()

    all_sorted_cities = []

    for i in index_list:
        ind = i[1]
        all_sorted_cities.append(all_cities[ind])

    return all_sorted_cities

def index(request):
    appid = '6a4f0328eeef57b74e12b8438db06807'
    print('!!!!!!!!!!!!!!!')
    #a = City(name='Toronto')
    #a.save()

    if request.method == 'POST':
        print('@@@@@@@@@@@@@@@@@@@@')
        form = CityForm(request.POST)
        form.save()
        return redirect('index')

    form = CityForm()

    cities = City.objects.all()

    all_cities = []
    for city in cities:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city.name}&units=metric&appid={appid}'
        res = requests.get(url).json()

        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }

        all_cities.append(city_info)

    all_sorted_cities = sort_info_by_temp(all_cities)

    context = {
        'all_info': all_sorted_cities,
        'form': form
    }

    return render(request, 'weather/index.html', context)

def add_city(request):
    print('333333333333333333555555555555555555')
    #return render(request, 'weather/index.html', {})
    #return render(request, 'weather/index.html', {})