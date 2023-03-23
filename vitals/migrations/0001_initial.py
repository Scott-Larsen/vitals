# Generated by Django 4.1.7 on 2023-03-23 01:28

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vitals",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_time", models.DateTimeField(verbose_name="Date recorded")),
                ("blood_pressure_systolic", models.IntegerField()),
                ("blood_pressure_diastolic", models.IntegerField()),
                (
                    "blood_pressure_position",
                    models.CharField(
                        choices=[("seat", "Seated"), ("stnd", "Standing")],
                        default="seat",
                        max_length=4,
                    ),
                ),
                ("pulse", models.IntegerField()),
                ("sp02", models.IntegerField()),
            ],
        ),
    ]
