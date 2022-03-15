from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all-coins', views.all_coins, name='all_coins'),
    path('coin-details/<str:coin_id>', views.coin_details, name='coin_details'),
    path('start-bot', views.start_bot, name='start_bot'),
]
