# Generated by Django 2.0.2 on 2018-04-28 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_player_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Team', verbose_name='time'),
        ),
    ]
