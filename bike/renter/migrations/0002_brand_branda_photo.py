# Generated by Django 5.0.7 on 2024-11-13 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='branda_photo',
            field=models.ImageField(default=0, upload_to='branda_photo/'),
            preserve_default=False,
        ),
    ]