import requests
from django.shortcuts import render
from .models import City

# Create your views here.



def index(request):
    appid = '6a4f0328eeef57b74e12b8438db06807'
    cities = City.objects.all()
    all_cityes = []

    for city in cities:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city.name}&units=metric&appid={appid}'
        res = requests.get(url).json()

        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }

        all_cityes.append(city_info)


    context = {
        'all_info': all_cityes
    }



    print("Данные:")

    for key in res.items():
        print(key)




    return render(request, 'weather/index.html', context)
