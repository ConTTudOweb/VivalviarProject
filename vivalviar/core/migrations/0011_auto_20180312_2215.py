# Generated by Django 2.0.2 on 2018-03-12 22:15

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20180310_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='logo',
            field=cloudinary.models.CloudinaryField(help_text='Imagem com: 350 X 350 pixels', max_length=255, verbose_name='logotipo'),
        ),
    ]
