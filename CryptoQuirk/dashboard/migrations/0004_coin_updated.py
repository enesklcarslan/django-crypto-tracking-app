# Generated by Django 4.0.3 on 2022-03-15 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_coin_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
