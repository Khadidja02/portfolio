# Generated by Django 5.0.6 on 2024-06-13 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_services_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='image',
        ),
        migrations.AddField(
            model_name='services',
            name='color_code',
            field=models.CharField(default='000000', max_length=7),
        ),
    ]