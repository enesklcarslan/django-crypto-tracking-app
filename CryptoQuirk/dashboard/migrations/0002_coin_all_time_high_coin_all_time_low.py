# Generated by Django 4.0.3 on 2022-03-14 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='all_time_high',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coin',
            name='all_time_low',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]