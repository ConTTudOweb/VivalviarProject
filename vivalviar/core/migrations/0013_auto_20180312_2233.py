# Generated by Django 2.0.2 on 2018-03-12 22:33

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20180312_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialparticipation',
            name='image',
            field=cloudinary.models.CloudinaryField(help_text='Imagem com: 300 X 300 pixels', max_length=255, verbose_name='imagem'),
        ),
    ]