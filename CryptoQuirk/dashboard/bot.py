from models import Coin, CoinHistory
import requests
from time import sleep
# coin_history_request = requests.get('https://api.coingecko.com/api/v3/coins/' + coin_id + '/market_chart?vs_currency=usd&days=30')
#     coin_history_data = coin_history_request.json()
#     coin_history_price = coin_history_data['prices']
#     coin_history_market_cap = coin_history_data['market_caps']
#     coin_history_volume = coin_history_data['volumes']
#     coin_history_change = coin_history_data['changes']
#     coin_history_date = coin_history_data['dates']
#     for i in range(len(coin_history_price)):
#         coin_history = CoinHistory(coin=Coin(id=coin_id, name=coin_name, symbol=coin_symbol), date=coin_history_date[i], price=coin_history_price[i], market_cap=coin_history_market_cap[i], volume=coin_history_volume[i], change=coin_history_change[i])
#         coin_history.save()
