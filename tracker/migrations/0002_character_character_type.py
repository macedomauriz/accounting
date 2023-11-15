# Generated by Django 4.2.7 on 2023-11-15 04:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tracker", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="character",
            name="character_type",
            field=models.CharField(
                choices=[("C", "peaches"), ("T", "birdos"), ("H", "marios")],
                default="C",
                max_length=1,
            ),
        ),
    ]