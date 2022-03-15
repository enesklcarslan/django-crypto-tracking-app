from dashboard.models import Coin, CoinHistory
import requests
from time import sleep
from datetime import datetime
from django.utils import timezone

from celery import shared_task

@shared_task
def update_coin_data():
    while True:
        coins_list = Coin.objects.all()
        for coin in coins_list:
            coin_id = coin.id
            print(coin_id)
            coin_request = requests.get('https://api.coingecko.com/api/v3/coins/' + coin_id)
            coin_data = coin_request.json()
            try:
                coin_current_price = coin_data['market_data']['current_price']['usd']
                coin_current_market_cap = coin_data['market_data']['market_cap']['usd']
                coin_current_volume = coin_data['market_data']['total_volume']['usd']
                coin_current_change = coin_data['market_data']['price_change_percentage_24h']
                Coin.objects.filter(id=coin_id).update(current_price=coin_current_price, current_market_cap=coin_current_market_cap, current_volume=coin_current_volume, current_change=coin_current_change, updated=datetime.now(tz=timezone.utc))
                CoinHistory.objects.create(coin=coin, price=coin_current_price, market_cap=coin_current_market_cap, volume=coin_current_volume, change=coin_current_change)
            except:
                print("Error updating coin " + coin_id)
            sleep(0.8)

