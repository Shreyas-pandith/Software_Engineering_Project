# Generated by Django 2.0.3 on 2018-03-12 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0023_auto_20180311_2226'),
        ('performance', '0010_auto_20180312_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performancematchwise',
            name='name',
        ),
        migrations.AddField(
            model_name='performancematchwise',
            name='match',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tournament.Match'),
        ),
    ]
