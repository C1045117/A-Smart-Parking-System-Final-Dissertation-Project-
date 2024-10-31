# Generated by Django 4.2.11 on 2024-05-06 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='parking_images/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]