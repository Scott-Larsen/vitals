# Generated by Django 4.1.7 on 2023-03-25 03:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("vitals", "0002_alter_vitals_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="vitals",
            old_name="sp02",
            new_name="spo2",
        ),
    ]