# Generated by Django 4.2.7 on 2024-01-17 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='location_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
