# Generated by Django 2.0.3 on 2018-03-12 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0036_auto_20180312_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scorecard',
            name='match',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tournament.Match'),
        ),
    ]
