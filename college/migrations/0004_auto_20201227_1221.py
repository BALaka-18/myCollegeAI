# Generated by Django 3.1.4 on 2020-12-27 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0003_auto_20201223_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='images',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='college',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
