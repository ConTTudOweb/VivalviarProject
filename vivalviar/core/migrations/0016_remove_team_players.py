# Generated by Django 2.0.2 on 2018-03-17 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_player_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='players',
        ),
    ]
