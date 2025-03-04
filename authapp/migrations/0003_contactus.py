# Generated by Django 5.1.5 on 2025-01-21 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_event_trackerentry_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('preferred_workout_time', models.CharField(blank=True, max_length=50, null=True)),
                ('message', models.TextField()),
            ],
        ),
    ]
