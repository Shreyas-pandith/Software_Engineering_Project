# Generated by Django 2.0.3 on 2018-03-12 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0034_scorecard_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scorecard',
            name='status',
        ),
    ]
