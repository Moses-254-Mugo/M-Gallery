# Generated by Django 3.2.8 on 2021-10-10 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='images',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='images',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]