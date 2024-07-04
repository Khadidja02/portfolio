# Generated by Django 5.0.6 on 2024-07-04 16:01

import webpages.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0004_remove_services_image_services_color_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='project_first_image',
            field=models.ImageField(blank=True, null=True, storage=webpages.storage.OverwriteStorage(), upload_to='project_pictures/'),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='image',
            field=models.ImageField(storage=webpages.storage.OverwriteStorage(), upload_to='project_pictures/'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=webpages.storage.OverwriteStorage(), upload_to='skill_pictures/'),
        ),
    ]
