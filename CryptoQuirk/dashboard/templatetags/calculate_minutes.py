from django import template
from datetime import datetime, timezone

register = template.Library()

def calculate_minutes(time):
    now = datetime.now(timezone.utc)
    #the time argument will be a datetime.datetime object
    delta = now - time
    minutes = delta.seconds // 60
    return minutes


register.filter('calculate_minutes', calculate_minutes)