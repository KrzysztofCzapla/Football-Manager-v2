# Generated by Django 4.2.7 on 2023-12-12 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_customuser_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='type_of_user',
        ),
    ]
