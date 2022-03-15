from django.shortcuts import render
from django.urls import reverse
from CoinUpdater.tasks import update_coin_data
from django.shortcuts import redirect
from time import sleep
from .models import Coin, CoinHistory
import requests

# Create your views here.
def index(request):
    context = {
        'coins': Coin.objects.order_by('-current_market_cap')[:8]
    }
    return render(request, 'dashboard/index.html', context)

def all_coins(request):
    context = {
        'coins': Coin.objects.order_by('-current_market_cap')
    }
    return render(request, 'dashboard/all_coins.html', context)

def coin_details(request, coin_id):
    coin = Coin.objects.get(id=coin_id)
    history = CoinHistory.objects.filter(coin=coin).order_by('date')
    context = {
        'coin': coin,
        'history': history
    }
    return render(request, 'dashboard/coin_details.html', context)

def start_bot(request):
    update_coin_data.delay()
    return redirect(reverse('index'))

