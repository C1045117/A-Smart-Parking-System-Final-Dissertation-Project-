# Generated by Django 4.2.11 on 2024-05-07 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(default='Reserved', max_length=10),
        ),
    ]