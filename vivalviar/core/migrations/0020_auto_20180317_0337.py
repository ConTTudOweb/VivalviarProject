# Generated by Django 2.0.2 on 2018-03-17 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20180317_0330'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ranking',
            options={'ordering': ('tournament', 'position'), 'verbose_name': 'classificação', 'verbose_name_plural': 'classificações'},
        ),
        migrations.AlterField(
            model_name='tournament',
            name='circuit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Circuit', verbose_name='circuito'),
        ),
    ]
