# Generated by Django 3.2.8 on 2021-10-10 14:48

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20211010_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
