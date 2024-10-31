# Generated by Django 4.2.11 on 2024-05-06 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.BinaryField()),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('parking_slot_label', models.TextField()),
            ],
        ),
    ]
