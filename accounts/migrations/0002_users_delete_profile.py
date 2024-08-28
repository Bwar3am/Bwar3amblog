# Generated by Django 5.0.7 on 2024-08-28 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('bio', models.CharField(max_length=500)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='pis/')),
            ],
        ),
        migrations.DeleteModel(
            name='profile',
        ),
    ]
