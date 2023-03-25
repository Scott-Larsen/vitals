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
    spo2 = models.IntegerField()

    def __str__(self):
        blood_pressure_position_verbose = [
            t[1] for t in self.POSITIONS if t[0] == self.blood_pressure_position]
        print(f"{blood_pressure_position_verbose = }")
        return " - ".join([
            f"{self.date_time.date()} {self.date_time.time()}",
            f"BP: {self.blood_pressure_systolic}/ {self.blood_pressure_diastolic} \
                ({blood_pressure_position_verbose[0]})",
            f"Pulse: {self.pulse}",
            f"SpO2: {self.spo2}",
        ])
