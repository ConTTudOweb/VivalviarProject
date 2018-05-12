# Generated by Django 2.0.2 on 2018-05-02 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_squashed_0024_auto_20180428_1759'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={},
        ),
        migrations.AddField(
            model_name='tournament',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='data'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='type',
            field=models.CharField(choices=[('O', 'Online'), ('P', 'Presencial')], default='O', max_length=1),
        ),
    ]