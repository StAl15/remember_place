# Generated by Django 4.0.4 on 2022-05-17 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=200, verbose_name='Место')),
                ('description', models.TextField(verbose_name='Комментарий')),
                ('url', models.SlugField(max_length=160)),
                ('latitude', models.FloatField(max_length=160, verbose_name='Широта')),
                ('longitude', models.FloatField(max_length=160, verbose_name='Долгота')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
            },
        ),
    ]
