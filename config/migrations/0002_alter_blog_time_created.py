# Generated by Django 5.0.7 on 2024-08-09 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='time_created',
            field=models.TimeField(auto_now=True),
        ),
    ]
