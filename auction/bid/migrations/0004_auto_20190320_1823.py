# Generated by Django 2.1.7 on 2019-03-20 12:53

from django.db import migrations, models
import django.utils.timezone
import pendulum


class Migration(migrations.Migration):

    dependencies = [
        ('bid', '0003_auto_20190320_0742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionitem',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='auctionitem',
            name='start_time',
        ),
        migrations.AddField(
            model_name='auctionitem',
            name='end_day',
            field=models.DateField(default=pendulum.tomorrow),
        ),
        migrations.AddField(
            model_name='auctionitem',
            name='start_day',
            field=models.DateField(default=django.utils.timezone.localdate),
        ),
    ]