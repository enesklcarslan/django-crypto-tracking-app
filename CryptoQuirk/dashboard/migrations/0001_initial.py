# Generated by Django 4.0.3 on 2022-03-14 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('symbol', models.CharField(max_length=10)),
                ('current_price', models.FloatField()),
                ('current_market_cap', models.FloatField()),
                ('current_volume', models.FloatField()),
                ('current_change', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CoinHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('price', models.FloatField()),
                ('market_cap', models.FloatField()),
                ('volume', models.FloatField()),
                ('change', models.FloatField()),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.coin')),
            ],
        ),
    ]