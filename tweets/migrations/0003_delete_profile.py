# Generated by Django 5.0 on 2024-01-05 07:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tweets", "0002_profile"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Profile",
        ),
    ]
