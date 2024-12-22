# Generated by Django 5.0.7 on 2024-12-20 10:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_fitnessdata_activity_level_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fitnessdata',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='fitnessdata',
            name='height',
            field=models.FloatField(default=170),
        ),
    ]
