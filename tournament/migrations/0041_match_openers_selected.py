# Generated by Django 2.0.1 on 2018-03-14 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0040_auto_20180314_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='openers_selected',
            field=models.BooleanField(default=False),
        ),
    ]
