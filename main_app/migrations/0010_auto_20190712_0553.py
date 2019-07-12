# Generated by Django 2.2.3 on 2019-07-12 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20190711_0758'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='accepted',
            field=models.IntegerField(default=0, verbose_name='Orders Accepted'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='total',
            field=models.IntegerField(default=0, verbose_name='Total Orders'),
        ),
    ]
