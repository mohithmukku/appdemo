# Generated by Django 5.0.3 on 2024-03-21 17:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdemo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='video',
            field=models.FileField(default=django.utils.timezone.now, upload_to='media/'),
            preserve_default=False,
        ),
    ]
