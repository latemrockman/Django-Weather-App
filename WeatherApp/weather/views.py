import requests
from django.shortcuts import render

# Create your views here.



def index(request):
    appid = '6a4f0328eeef57b74e12b8438db06807'
    city = 'Moscow'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={appid}'

    res = requests.get(url).json()

    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon']
    }

    context = {
        'info': city_info
    }

    print("Данные:")

    for key in res.items():
        print(key)




    return render(request, 'weather/index.html', context)
