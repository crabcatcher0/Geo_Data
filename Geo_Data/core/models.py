from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    longitutude = models.FloatField(null=False, default=0, blank=False)
    latitude = models.FloatField(null=False, blank=False, default=0)

    def __str__(self):
        return self.name


class Hospital(models.Model):
    hospital_name = models.CharField(max_length=100)
    in_city = models.ForeignKey("City", on_delete=models.CASCADE)  # type: ignore
    longitude = models.FloatField(default=0, null=False, blank=False)
    latitude = models.FloatField(default=0, null=False, blank=False)

    def __str__(self):
        return self.hospital_name
