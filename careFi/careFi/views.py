from wsgiref import headers
from django.http import HttpResponse, JsonResponse, request
from .models import bitCoinPrice
from .serializers import BitcoinPriceSerializer
import requests
import json

API_KEY = "C1625BC9-8888-4D6E-A345-0F8DD3BDF277"

def get_price(request):

    url = "https://rest.coinapi.io/v1/exchangerate/BTC/INR"
    headers = {
        "X-CoinAPI-Key" : API_KEY
    }

    response = requests.get(url, headers= headers).json()
    
    price = response['rate']
    time = response['time']

    obj = bitCoinPrice()
    obj.price = price
    obj.time = time
    obj.save()

    response_dict = {
        "price" : price,
        "time" : time
    }

    return JsonResponse(response_dict)    
