# Generated by Django 2.0.2 on 2018-03-10 21:35

from django.db import migrations
import versatileimagefield.fields
import vivalviar.core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20180310_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(help_text='Imagem com: 873 X 1280 pixels', verbose_name='imagem'),
        ),
    ]