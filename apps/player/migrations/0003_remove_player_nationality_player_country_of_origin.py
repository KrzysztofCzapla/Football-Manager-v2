# Generated by Django 4.2.7 on 2023-12-08 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('player', '0002_player_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='nationality',
        ),
        migrations.AddField(
            model_name='player',
            name='country_of_origin',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.country'),
        ),
    ]
