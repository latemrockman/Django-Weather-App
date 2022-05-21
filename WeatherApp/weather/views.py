import requests
from django.shortcuts import render

# Create your views here.



def index(request):
    appid = '6a4f0328eeef57b74e12b8438db06807'
    city = 'Moscow'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}'

    res = requests.get(url)




    return render(request, 'weather/index.html')
