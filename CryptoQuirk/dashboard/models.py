from django.db import models

# Create your models here.
class Coin(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    logo = models.URLField(null=True)
    current_price = models.FloatField()
    current_market_cap = models.FloatField()
    current_volume = models.FloatField()
    current_change = models.FloatField()
    all_time_high = models.FloatField()
    all_time_low = models.FloatField()
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name + " (" + self.symbol + ")"

class CoinHistory(models.Model):
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    market_cap = models.FloatField()
    volume = models.FloatField()
    change = models.FloatField()

    def __str__(self):
        return self.coin.name + " (" + self.coin.symbol + ") - " + str(self.date)