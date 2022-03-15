from django.contrib import admin
from .models import Coin, CoinHistory

# Register your models here.
class CoinAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'symbol', 'current_price', 'current_market_cap', 'current_volume', 'current_change')
    list_filter = ('id', 'name', 'symbol', 'current_price', 'current_market_cap', 'current_volume', 'current_change')
    search_fields = ('id', 'name', 'symbol', 'current_price', 'current_market_cap', 'current_volume', 'current_change')

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('coin', 'date', 'price', 'market_cap', 'volume', 'change')
    list_filter = ('coin', 'date', 'price', 'market_cap', 'volume', 'change')
    search_fields = ('coin', 'date', 'price', 'market_cap', 'volume', 'change')

admin.site.register(Coin, CoinAdmin)
admin.site.register(CoinHistory, HistoryAdmin)