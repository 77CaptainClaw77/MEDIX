# Generated by Django 2.2.3 on 2019-07-09 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20190708_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
