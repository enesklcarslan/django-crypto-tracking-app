# Django Crypto Tracking App

A Django app for tracking crypto currency prices using CoinGecko API.

## Requirements
Needs [RabbitMQ](https://github.com/rabbitmq/rabbitmq-server/releases/tag/v3.9.13) installed to run Celery, in order to update and store prices from CoinGecko API.

## How to run

 - ### Firstly, run:

`pip install -r requirements.txt`

 - ### Then:
`cd CryptoQuirk` 
`python manage.py runserver`

 - ### Open another terminal and run:
`celery -A CryptoQuirk worker --loglevel=INFO --concurrency 1 -P solo`

Then everything should work correctly.

## Todo

 - [ ] Add htmx support to dynamically refresh homepage and all coin prices
 - [ ] Ajax to dynamically refresh chart data from serverside endpoints
