from django.db import models


class Vitals(models.Model):
    class Meta:
        verbose_name_plural = "Vitals"

    POSITIONS = (
        ("seat", "Seated"),
        ("stnd", "Standing"),
    )

    date_time = models.DateTimeField('Date recorded')
    blood_pressure_systolic = models.IntegerField()
    blood_pressure_diastolic = models.IntegerField()
    blood_pressure_position = models.CharField(
        max_length=4, choices=POSITIONS, default="seat")
    pulse = models.IntegerField()
    sp02 = models.IntegerField()
