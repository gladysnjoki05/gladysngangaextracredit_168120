# Generated by Django 5.1.3 on 2024-12-22 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=10, unique=True)),
                ('departure', models.DateTimeField()),
                ('arrival', models.DateTimeField()),
                ('origin', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passengers', to='bookings.flight')),
            ],
        ),
    ]
